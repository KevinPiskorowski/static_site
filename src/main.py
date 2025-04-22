import os
import shutil
import sys

from copystatic import copy_files_recursive
from pagegenerate import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_template = "./template.html"
dir_path_content = "./content"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, dir_path_template, dir_path_public, basepath)
    
if __name__ =="__main__":
    main()

