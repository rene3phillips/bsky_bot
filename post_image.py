import os  # Import the os module for interacting with the operating system
import json  # Import the JSON module for working with JSON data
from resize_image import resize_image  # Import the resize_image function to resize images

# Load the content list from the JSON file
def load_content_from_json():
    try:
        # Define the file path of the JSON file containing the content
        file_path = 'data/post_image.json'
        
        # Check if the file exists before attempting to open it
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return []  # Return an empty list if the file is not found
        
        # Open and load the JSON content
        with open(file_path, 'r', encoding='utf-8') as f:  # Specify UTF-8 encoding to read the file
            content_list = json.load(f)  # Load the content from the file
        
        print(f"Loaded content: {content_list}")  # Debugging line to print the loaded content
        return content_list  # Return the loaded content
    except Exception as e:
        # If an error occurs during loading, print the error and return an empty list
        print(f"Error loading JSON file: {e}")
        return []

# Initialize global index for tracking current content
current_image_index = 0  # This variable tracks the current content to post

def post_image(client):
    """Post the next item in the CONTENT_LIST sequentially."""
    global current_image_index  # Access the global variable for current image index

    # Load content list from the JSON file
    content_list = load_content_from_json()
    
    if not content_list:
        # If no content is available, print a message and exit the function
        print("No content to post.")
        return

    try:
        # Get the current content to post
        content = content_list[current_image_index]  # Access the content using the current index
        text = content["text"]  # Extract the text content
        image_path = content["image_path"]  # Extract the image path

        # Resize the image using the resize_image function
        resized_image_path = resize_image(image_path, f"resized_{os.path.basename(image_path)}", target_size_mb=1, folder_path="images")

        # Open the resized image and read its binary data
        with open(resized_image_path, 'rb') as f:
            img_data = f.read()
        
        # Send the image along with the text as a post
        client.send_image(text=text, image=img_data, image_alt='90s Content')
        print(f"Posted content: {text}")  # Print the success message

        # Update the index to the next item, and reset if we've reached the end of the list
        current_image_index = (current_image_index + 1) % len(content_list)

    except Exception as e:
        # If an error occurs while posting content, print the error message
        print("An error occurred while posting content:", e)

