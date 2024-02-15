from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(512, 512)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        # Construct the input and output file paths
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        try:
            # Open the image file
            img = Image.open(input_path)

            # Resize the image
            img = img.resize(target_size)

            # Save the resized image
            img.save(output_path)

            print(f"Resized {file_name} successfully.")
        except Exception as e:
            print(f"Error resizing {file_name}: {e}")

if __name__ == "__main__":
    # Input and output folder paths
    input_folder = "val_images"
    output_folder = "3"

    # Call the resize function
    resize_images(input_folder, output_folder)
