import os
import argparse

def list_files(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=True):
        for name in files:
            print(os.path.join(root, name).replace(os.sep, '/'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List files in a directory")
    parser.add_argument("root_directory", nargs='?', default=None, help="Root directory to list files from")
    args = parser.parse_args()

    if args.root_directory is None:
        print("Directory is not specified")
    else:
        list_files(args.root_directory)
