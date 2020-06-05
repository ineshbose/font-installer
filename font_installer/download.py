import requests, zipfile, os, argparse


parser = argparse.ArgumentParser()
parser.add_argument('url', help="URL of the font")
parser.add_argument('-k','--keep', help="Keep files", action="store_true")
parser.add_argument('-v', '--verbose', help="Output execution details", action="store_true")
args = parser.parse_args()

if os.name == 'nt':
    from font_installer.windows import install_font
elif os.name == 'posix':
    from font_installer.posix import install_font
else:
    print("OS not supported!")
    exit()


def download(url, chunk_size=128):
    if 'www.dafont.com' in url:
        font_name = url.replace("-","_").split("www.dafont.com/")[1].split('.font')[0]
        dl_url = "https://dl.dafont.com/dl/?f={}".format(font_name)
    elif 'fonts.google.com' in url:
        font_name = url.replace("+","%20").split("fonts.google.com/specimen/")[1]
        dl_url = "https://fonts.google.com/download?family={}".format(font_name)
    r = requests.get(dl_url, stream=True)
    
    if args.verbose: print("Saving ZIP..")
    # save ZIP
    with open(font_name+".zip", 'wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)

    if args.verbose: print("Extracting from ZIP..")
    # extract ZIP
    with zipfile.ZipFile(font_name+".zip", 'r') as zip_ref:
        zip_ref.extractall(font_name)
    
    if args.verbose: print("Installing..")
    # install
    try:
        for f in os.listdir(font_name):
            if '.otf' in f.lower() or '.ttf' in f.lower():
                install_font(os.path.abspath(font_name+"/"+f))
    
    except PermissionError:
        print("Permission Error thrown. Did you run as Administrator?")

    # delete files
    if not args.keep:
        if args.verbose: print("Deleting files..")
        os.remove(font_name+".zip")
        try:
            os.rmdir(font_name)
        except OSError:
            for f in os.listdir(font_name):
                os.remove(font_name+"/"+f)
            os.rmdir(font_name)

def main():
    download(args.url)