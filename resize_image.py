import os
from PIL import Image # use to open image files

def resize_image(input_path, output_filename, target_size_mb=1, folder_path="images"):
    """
    Resize the image to ensure it's under a specified size and save it to the specified folder.
    
    Parameters:
        input_path (str): The path to the input image.
        output_filename (str): The name of the output image file.
        target_size_mb (float): The target size in MB (default: 1 MB).
        folder_path (str): The folder where the image should be saved (default: "images").
    """
    
    # Construct the full output path by joining the folder path and output filename
    output_path = os.path.join(folder_path, output_filename)
    
    # Open the image file using PIL (Python Imaging Library)
    img = Image.open(input_path)

    # Get original image size in bytes and convert it to MB
    file_size = os.path.getsize(input_path) / (1024 * 1024)  # Size in MB

    # If the image is already smaller than the target size, just return the original image
    if file_size <= target_size_mb:
        print(f"\nImage is already {file_size:.2f} MB, which is under {target_size_mb} MB.")
        img.save(output_path)  # Save the image without resizing
        return output_path

    # Start resizing by reducing dimensions, and reduce quality if needed, until the file size is under target
    quality = 90  # Initial quality level (starts at 90%)
    
    while file_size > target_size_mb:
        # Resize image (reduce dimensions to half of the current width and height)
        img = img.resize((img.width // 2, img.height // 2), Image.Resampling.LANCZOS)

        # Save the image with reduced quality to the output path
        img.save(output_path, quality=quality)

        # Check the file size after saving the resized image
        file_size = os.path.getsize(output_path) / (1024 * 1024)

        # If file size is still too large, reduce quality further
        if file_size > target_size_mb:
            quality -= 5  # Decrease quality to compress further

    # Print out the final file size and the location where the image is saved
    print(f"\nImage resized to {file_size:.2f} MB and saved as {output_path}")
    return output_path

