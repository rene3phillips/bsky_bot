import os
from PIL import Image

def resize_image(input_path, output_filename, target_size_mb=1, folder_path="images"):
    """
    Resize the image to ensure it's under a certain size and save it to the specified folder.
    
    Parameters:
        input_path (str): The path to the input image.
        output_filename (str): The name of the output image file.
        target_size_mb (float): The target size in MB (default: 1 MB).
        folder_path (str): The folder where the image should be saved (default: "images").
    """
    
    # Construct the full output path
    output_path = os.path.join(folder_path, output_filename)
    
    # Open the image file
    img = Image.open(input_path)

    # Get original image size in bytes
    file_size = os.path.getsize(input_path) / (1024 * 1024)  # Size in MB

    # If the image is already smaller than 1 MB, just return it
    if file_size <= target_size_mb:
        print(f"Image is already {file_size:.2f} MB, which is under 1 MB.")
        img.save(output_path)
        return output_path

    # Start resizing by a factor, e.g., reducing by 10% until under target size
    quality = 90
    while file_size > target_size_mb:
        # Resize image (reduce quality or dimensions)
        img = img.resize((img.width // 2, img.height // 2), Image.Resampling.LANCZOS)

        # Save the image with reduced quality to the output path
        img.save(output_path, quality=quality)

        # Check the file size after saving
        file_size = os.path.getsize(output_path) / (1024 * 1024)

        # Reduce quality if needed
        if file_size > target_size_mb:
            quality -= 5  # Decrease quality to compress further

    print(f"Image resized to {file_size:.2f} MB and saved as {output_path}")
    return output_path

def resize_all_images_in_folder(folder_path="images", target_size_mb=1):
    """Resize all images in the specified folder to ensure they are under the target size."""
    # List all files in the folder
    for filename in os.listdir(folder_path):
        # Get full file path
        file_path = os.path.join(folder_path, filename)

        # Only process image files (e.g., .jpg, .jpeg, .png)
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            print(f"Processing {filename}...")
            # Generate output filename (you can modify this as needed)
            output_filename = f"{filename}"
            # Resize the image
            resize_image(file_path, output_filename, target_size_mb, folder_path)

# Example usage: Resize all images in the "images" folder
resize_all_images_in_folder(folder_path="images", target_size_mb=1)
