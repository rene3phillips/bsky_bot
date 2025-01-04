import schedule  # Import the schedule module to run tasks at specific times
from shared import authenticate, log_activity, wait_and_run  # Import shared functions for authentication, logging, and task scheduling
from post_image import post_image  # Import the function to post an image
from post_text import post_text  # Import the function to post text content
from like import like_recent_posts  # Import the function to like recent posts
from follow import follow_from_feed_generator  # Import the function to follow authors from a feed

# Authenticate client
client = authenticate()  # Authenticate and return a logged-in client

# Wrappers for tasks with logging
def post_image_with_log():
    """Post an image and log the activity."""
    post_image(client)  # Post an image using the client
    log_activity("Image posted")  # Log the activity of posting an image

def post_text_with_log():
    """Post text content and log the activity."""
    post_text(client)  # Post text content using the client
    log_activity("Text content posted")  # Log the activity of posting text content

def like_posts_with_log():
    """Like recent posts and log the activity."""
    like_recent_posts(client)  # Like recent posts using the client
    log_activity("Liked recent posts")  # Log the activity of liking posts

def follow_with_log():
    """Follow authors from a feed generator and log the activity."""
    feed_generator_uri = "at://did:plc:xatbuopfl7g3dht7vhzpvv5x/app.bsky.feed.generator/aaacdps7yadba"  # URI for the feed generator
    follow_from_feed_generator(client, feed_generator_uri, max_to_follow=5, preferred_languages="en-US")  # Follow authors from the feed
    log_activity("Followed authors from feed")  # Log the activity of following authors

# Schedule tasks
schedule.every().day.at("10:03").do(post_text_with_log)  
schedule.every().day.at("10:04").do(post_image_with_log)  
schedule.every().day.at("10:05").do(like_posts_with_log) 
schedule.every().day.at("10:06").do(follow_with_log)  

print("\nAll tasks have been scheduled.")  # Print confirmation that all tasks are scheduled

wait_and_run()  # Keep the scheduler running in an infinite loop to execute tasks at their scheduled times

