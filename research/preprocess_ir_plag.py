import os
import pandas as pd
import shutil  # Import shutil for file copying

data = pd.DataFrame(columns=["id1", "id2", "plagio", "caseId"])

DATASET_PATH = "datasets/ir_plag"
TARGET_PATH = "datasets/ir_plag_preprocessed"

ORIGINAL_DIR_NAME = "original"
PLAGIARIZED_DIR_NAME = "plagiarized"
NON_PLAGIARIZED_DIR_NAME = "non-plagiarized"

curr_id = 0

for dir_name in os.listdir(DATASET_PATH):
    dir_path = os.path.join(DATASET_PATH, dir_name)
    case_id = dir_name.split("-")[1]

    if not os.path.isdir(dir_path):
        print(f"Skipping {dir_path} as it is not a directory")
        continue

    original_file_path = os.path.join(dir_path, ORIGINAL_DIR_NAME)
    files = os.listdir(original_file_path)

    if len(files) > 1:
        print(f"More than one original file in {dir_path}. Expected only one")
        continue

    original_file = files[0]
    original_file_path = os.path.join(original_file_path, original_file)

    if not os.path.isfile(original_file_path):
        print(f"Original file {original_file_path} does not exist")
        continue

    # Copy the original file to the target directory
    new_file_name = f"{curr_id}.{original_file.split('.')[-1]}"
    original_file_id = curr_id
    curr_id += 1
    new_file_path = os.path.join(TARGET_PATH, new_file_name)
    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
    shutil.copy(original_file_path, new_file_path)

    plagiarized_levels_dirs = os.listdir(
        os.path.join(dir_path, PLAGIARIZED_DIR_NAME))
    plagiarized_file_paths = []
    for plagiarized_level_dir in plagiarized_levels_dirs:
        plagiarized_dir = os.path.join(
            dir_path, PLAGIARIZED_DIR_NAME, plagiarized_level_dir)
        if not os.path.isdir(plagiarized_dir):
            print(f"Skipping {plagiarized_dir} as it is not a directory")
            continue
        plagiarized_dirs = os.listdir(plagiarized_dir)

        for plagiarized_dir in plagiarized_dirs:
            plagiarized_files = os.path.join(
                dir_path, PLAGIARIZED_DIR_NAME, plagiarized_level_dir, plagiarized_dir)
            if not os.path.isdir(plagiarized_files):
                print(f"Skipping {plagiarized_files} as it is not a directory")
                continue

            files = os.listdir(plagiarized_files)
            if len(files) > 1:
                print(
                    f"More than one plagiarized file in {plagiarized_files}. Expected only one")
                print(files)
                continue

            plagiarized_file = os.listdir(plagiarized_files)[0]
            plagiarized_file_path = os.path.join(
                plagiarized_files, plagiarized_file)
            if not os.path.isfile(plagiarized_file_path):
                print(
                    f"Plagiarized file {plagiarized_file_path} does not exist")
                continue
            plagiarized_file_paths.append(plagiarized_file_path)

    for plagiarized_file_path in plagiarized_file_paths:
        if not os.path.isfile(plagiarized_file_path):
            print(f"Plagiarized file {plagiarized_file_path} does not exist")
            continue

        # Copy the plagiarized file to the target directory
        new_file_name = f"{curr_id}.{plagiarized_file_path.split('.')[-1]}"
        curr_id += 1
        new_file_path = os.path.join(TARGET_PATH, new_file_name)
        os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
        shutil.copy(plagiarized_file_path, new_file_path)

        # Append the data to the DataFrame
        data = data._append({
            "id1": original_file_id,
            "id2": curr_id,
            "plagio": 1,
            "caseId": case_id
        }, ignore_index=True)

    non_plagiarized_dirs = os.listdir(
        os.path.join(dir_path, NON_PLAGIARIZED_DIR_NAME))
    non_plagiarized_file_paths = []
    for non_plagiarized_dir in non_plagiarized_dirs:
        non_plagiarized_files = os.path.join(
            dir_path, NON_PLAGIARIZED_DIR_NAME, non_plagiarized_dir)
        if not os.path.isdir(non_plagiarized_files):
            print(f"Skipping {non_plagiarized_files} as it is not a directory")
            continue

        if len(os.listdir(non_plagiarized_files)) > 1:
            print(
                f"More than one non-plagiarized file in {non_plagiarized_files}. Expected only one")
            continue

        non_plagiarized_file = os.listdir(non_plagiarized_files)[0]
        non_plagiarized_file_path = os.path.join(
            non_plagiarized_files, non_plagiarized_file)
        if not os.path.isfile(non_plagiarized_file_path):
            print(
                f"Non-plagiarized file {non_plagiarized_file_path} does not exist")
            continue
        non_plagiarized_file_paths.append(non_plagiarized_file_path)

    for non_plagiarized_file_path in non_plagiarized_file_paths:
        if not os.path.isfile(non_plagiarized_file_path):
            print(
                f"Non-plagiarized file {non_plagiarized_file_path} does not exist")
            continue

        # Copy the non-plagiarized file to the target directory
        new_file_name = f"{curr_id}.{non_plagiarized_file_path.split('.')[-1]}"
        curr_id += 1
        new_file_path = os.path.join(TARGET_PATH, new_file_name)
        os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
        shutil.copy(non_plagiarized_file_path, new_file_path)

        # Append the data to the DataFrame
        data = data._append({
            "id1": original_file_id,
            "id2": curr_id,
            "plagio": 0,
            "caseId": case_id
        }, ignore_index=True)

# Save the DataFrame to a CSV file
data.to_csv("ir_plag_labels.csv", index=False)
