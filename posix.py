import os

def install_font(src_path):

    # create
    try:
        os.mkdir("~/.fonts")
    except FileExistsError:
        pass

    # move files
    os.rename(src_path, "~/.fonts/"+src_path.split('/')[-1])