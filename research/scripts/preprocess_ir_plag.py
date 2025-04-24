from pathlib import Path
import pandas as pd
import shutil

data = pd.DataFrame(columns=["id1", "id2", "plagio", "caseId"])

DATASET_PATH = Path("../datasets/ir_plag")
TARGET_PATH = Path("../datasets/ir_plag_preprocessed")

ORIGINAL_DIR_NAME = "original"
PLAGIARIZED_DIR_NAME = "plagiarized"
NON_PLAGIARIZED_DIR_NAME = "non-plagiarized"

curr_id = 0

for dir_path in DATASET_PATH.iterdir():
    if not dir_path.is_dir():
        print(f"Skipping {dir_path} as it is not a directory")
        continue

    case_id = dir_path.name.split("-")[1]
    original_file_path = dir_path / ORIGINAL_DIR_NAME
    files = list(original_file_path.iterdir())

    if len(files) > 1:
        print(f"More than one original file in {dir_path}. Expected only one")
        continue

    original_file = files[0]

    if not original_file.is_file():
        print(f"Original file {original_file} does not exist")
        continue

    # Copy the original file to the target directory
    new_file_name = f"{curr_id}.{original_file.suffix.lstrip('.')}"
    original_file_id = curr_id
    curr_id += 1
    new_file_path = TARGET_PATH / new_file_name
    new_file_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(original_file, new_file_path)

    plagiarized_levels_dirs = (dir_path / PLAGIARIZED_DIR_NAME).iterdir()
    plagiarized_file_paths = []
    for plagiarized_level_dir in plagiarized_levels_dirs:
        if not plagiarized_level_dir.is_dir():
            print(f"Skipping {plagiarized_level_dir} as it is not a directory")
            continue

        for plagiarized_dir in plagiarized_level_dir.iterdir():
            if not plagiarized_dir.is_dir():
                print(f"Skipping {plagiarized_dir} as it is not a directory")
                continue

            files = list(plagiarized_dir.iterdir())
            if len(files) > 1:
                print(
                    f"More than one plagiarized file in {plagiarized_dir}. Expected only one")
                print(files)
                continue

            plagiarized_file = files[0]
            if not plagiarized_file.is_file():
                print(f"Plagiarized file {plagiarized_file} does not exist")
                continue
            plagiarized_file_paths.append(plagiarized_file)

    for plagiarized_file_path in plagiarized_file_paths:
        if not plagiarized_file_path.is_file():
            print(f"Plagiarized file {plagiarized_file_path} does not exist")
            continue

        # Copy the plagiarized file to the target directory
        new_file_name = f"{curr_id}.{plagiarized_file_path.suffix.lstrip('.')}"
        curr_id += 1
        new_file_path = TARGET_PATH / new_file_name
        new_file_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(plagiarized_file_path, new_file_path)

        # Append the data to the DataFrame
        data = data._append({
            "id1": original_file_id,
            "id2": curr_id,
            "plagio": 1,
            "caseId": case_id
        }, ignore_index=True)

    non_plagiarized_dirs = (dir_path / NON_PLAGIARIZED_DIR_NAME).iterdir()
    non_plagiarized_file_paths = []
    for non_plagiarized_dir in non_plagiarized_dirs:
        if not non_plagiarized_dir.is_dir():
            print(f"Skipping {non_plagiarized_dir} as it is not a directory")
            continue

        files = list(non_plagiarized_dir.iterdir())
        if len(files) > 1:
            print(
                f"More than one non-plagiarized file in {non_plagiarized_dir}. Expected only one")
            continue

        non_plagiarized_file = files[0]
        if not non_plagiarized_file.is_file():
            print(
                f"Non-plagiarized file {non_plagiarized_file} does not exist")
            continue
        non_plagiarized_file_paths.append(non_plagiarized_file)

    for non_plagiarized_file_path in non_plagiarized_file_paths:
        if not non_plagiarized_file_path.is_file():
            print(
                f"Non-plagiarized file {non_plagiarized_file_path} does not exist")
            continue

        # Copy the non-plagiarized file to the target directory
        new_file_name = f"{curr_id}.{non_plagiarized_file_path.suffix.lstrip('.')}"
        curr_id += 1
        new_file_path = TARGET_PATH / new_file_name
        new_file_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(non_plagiarized_file_path, new_file_path)

        # Append the data to the DataFrame
        data = data._append({
            "id1": original_file_id,
            "id2": curr_id,
            "plagio": 0,
            "caseId": case_id
        }, ignore_index=True)

# Save the DataFrame to a CSV file
data.to_csv("../labels/ir_plag_labels.csv", index=False)
