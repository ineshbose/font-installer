from download import download
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', help="URL of the font")

if __name__ == '__main__':
    args = parser.parse_args()
    download(args.url)