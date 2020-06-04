import requests, zipfile, os, argparse


parser = argparse.ArgumentParser()
parser.add_argument('url', help="URL of the font")


def download(url, chunk_size=128):
    font_name = url.replace("-","_").split("https://www.dafont.com/")[1].split('.font')[0]
    dl_url = "https://dl.dafont.com/dl/?f={}".format(font_name)
    r = requests.get(dl_url, stream=True)
    
    # save ZIP
    with open(font_name+".zip", 'wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)

    # extract ZIP
    with zipfile.ZipFile(font_name+".zip", 'r') as zip_ref:
        zip_ref.extractall(font_name)

    # install
    try:
        
        for f in os.listdir(font_name):
            if '.otf' in f or '.ttf' in f:

                if os.name == 'nt':
                    import windows
                    windows.install_font(os.path.abspath(font_name+"/"+f))
                elif os.name == 'posix':
                    import posix
                    posix.install_font()
                else:
                    print("OS not supported!")
    
    except PermissionError:
        print("Permission Error thrown. Did you run as Administrator?")

    # delete files
    os.remove(font_name+".zip")
    try:
        os.rmdir(font_name)
    except OSError:
        for f in os.listdir(font_name):
            os.remove(font_name+"/"+f)
        os.rmdir(font_name)

def main():
    args = parser.parse_args()
    download(args.url)