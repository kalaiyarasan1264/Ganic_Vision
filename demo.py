import subprocess
import sys

def run_command(command):
    """
    Run a shell command and check if it completes successfully.
    """
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}: {command}")
        sys.exit(1)
    else:
        print(f"Command succeeded: {command}")

def main():
    # Step 1: Run the first test.py script with the given parameters
    print("Starting image Reconstruction...")
    command1 = (
        "python D:/workspacee/Ganic_Vision/Image_reconstruction/test.py --checkpoints D:/workspacee/Ganic_Vision/Image_reconstruction/checkpoints/places2 "
        "--input C:/Users/kalki/OneDrive/Desktop/Input/images "
        "--mask C:/Users/kalki/OneDrive/Desktop/Input/masks "
        "--output C:/Users/kalki/OneDrive/Desktop/Output/Image_Reconstruction-Output"
    )
    run_command(command1)

    # Step 2: Run the second test.py script with the output from the first script as input
    print("Completed Image Reconstruction. Starting Image Attribute Manipulation...")
    command2 = (
        "python D:/workspacee/Ganic_Vision/Attribute_manipulation/test.py --img_root C:/Users/kalki/OneDrive/Desktop/Output/Image_Reconstruction-Output "
        "--text_file D:/workspacee/Ganic_Vision/Attribute_manipulation/test/text_flowers.txt "
        "--fasttext_model D:/workspacee/Ganic_Vision/Attribute_manipulation/models/wiki.en.bin "
        "--generator_model D:/workspacee/Ganic_Vision/Attribute_manipulation/models/flowers_G.pth "
        "--org_root C:/Users/kalki/OneDrive/Desktop/Input/images "
        "--output_root C:/Users/kalki/OneDrive/Desktop/Output/Final_Output"
    )
    run_command(command2)

    print("Completed both processes and saved final output.")

if __name__ == "__main__":
    main()
