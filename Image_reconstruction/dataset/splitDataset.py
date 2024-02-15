import os
import random
from shutil import copyfile

def split_dataset(input_folder, output_folder, train_ratio=0.7, test_ratio=0.15, val_ratio=0.15):
    # Create output folders if they don't exist
    train_folder = os.path.join(output_folder, 'train')
    test_folder = os.path.join(output_folder, 'test')
    val_folder = os.path.join(output_folder, 'val')

    for folder in [train_folder, test_folder, val_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Get list of files
    files = os.listdir(input_folder)
    num_files = len(files)
    random.shuffle(files)

    # Calculate the number of files for each set
    train_end = int(train_ratio * num_files)
    test_end = int(test_ratio * num_files) + train_end

    # Copy files to respective sets
    for i, file_name in enumerate(files):
        input_path = os.path.join(input_folder, file_name)

        if i < train_end:
            output_path = os.path.join(train_folder, file_name)
        elif i < test_end:
            output_path = os.path.join(test_folder, file_name)
        else:
            output_path = os.path.join(val_folder, file_name)

        try:
            copyfile(input_path, output_path)
            print(f"Copied {file_name} to {output_path} successfully.")
        except Exception as e:
            print(f"Error copying {file_name}: {e}")

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"

    split_dataset(input_folder, output_folder)
