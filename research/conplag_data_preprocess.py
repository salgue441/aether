import os
import shutil

files_path = "./research/datasets/conplag"  # Path to the directory containing the files
destination_path = "./research/datasets/conplag_preprocessed"

os.makedirs(destination_path, exist_ok=True)

files_dict = {}

# Traverse the directory structure and collect unique files
for dir in os.listdir(files_path):
    for file in os.listdir(os.path.join(files_path, dir)):
        if file.endswith(".java") and file not in files_dict:
            files_dict[file] = os.path.join(files_path, dir, file)

print(f"{len(files_dict)} unique files found.")

files_set = set(files_dict.values())

print("Copying files...")
# Copy files to the destination directory
for file in files_set:
    shutil.copy(file, destination_path)

print(f"{len(files_set)} files copied successfully to '{destination_path}'.")
