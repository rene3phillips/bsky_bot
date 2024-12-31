import json  # Import the JSON module for working with JSON data

# Load the content list from the JSON file
def load_text_content_from_json():
    try:
        # Attempt to open the JSON file and load the content into the list
        with open('data/post_text.json', 'r', encoding='utf-8') as f:
            content_list = json.load(f)  # Load the content from the file into a Python list
        return content_list  # Return the loaded content list
    except Exception as e:
        # If an error occurs, print the error message and return an empty list
        print(f"Error loading JSON file: {e}")
        return []

# Global index to track current content
current_index = 0  # Initialize the index to track which post to send next

def post_text(client):
    """Post text from the loaded content list."""
    global current_index  # Access the global variable for the current index

    # Load content list from the JSON file
    content_list = load_text_content_from_json()
    
    if not content_list:
        # If no content is loaded, print a message and return from the function
        print("No content to post.")
        return

    try:
        # Get the content to post from the list using the current index
        text_content = content_list[current_index]["text"]
        
        # Send the post using the client object
        client.send_post(text=text_content)
        print(f"Successfully posted: {text_content}")  # Print success message

        # Update the index to point to the next post, and reset if we've reached the end of the list
        current_index = (current_index + 1) % len(content_list)

    except Exception as e:
        # If an error occurs while posting the content, print the error message
        print(f"Error posting content: {e}")

