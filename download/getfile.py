# Gets a link, a filepath with included filenamne and downloads the target with wget

import sys
import wget
import os

# Check if args provided, if not explain usage
if len(sys.argv) < 2:
    print("getfile.py > No link provided, please proved a download link and a filepath.")
    exit()

# Remove filename from filepath
filepath = sys.argv[2].split('/')
folder_path = '/'.join(filepath[:-1])  # Join the list back into a string
print("Folder path = " + folder_path)

# Check if the folder exists, if not create it
if len(filepath) > 1:
    folder = '/'.join(filepath[:-1])
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder {folder}")


# If file exists in the path, delete it
if os.path.exists(sys.argv[2]):
    os.remove(sys.argv[2])
    print(f"Deleted {sys.argv[2]}")
    
# Download the file with wget into the filepath
wget.download(sys.argv[1], sys.argv[2])
print(f"Downloaded {sys.argv[1]} to {sys.argv[2]}")