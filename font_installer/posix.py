import os

def install_font(src_path):

    dr = os.path.expanduser('~/.fonts')

    # create
    try:
        os.mkdir(dr)
    except FileExistsError:
        pass

    # move files
    os.rename(src_path, dr+src_path.split('/')[-1])