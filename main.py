import schedule
from shared import authenticate, log_activity, wait_and_run
from post_image import post_image
from post_text import post_text
from like import like_recent_posts
from follow import follow_from_feed_generator
from resize_image import resize_all_images_in_folder  

# Authenticate client
client = authenticate()

# Wrappers for tasks with logging
def post_image_with_log():
    post_image(client)
    log_activity("Image posted")

def post_text_with_log():
    post_text(client)
    log_activity("Text content posted")

def like_posts_with_log():
    like_recent_posts(client)
    log_activity("Liked recent posts")

def follow_with_log():
    feed_generator_uri = "at://did:plc:xatbuopfl7g3dht7vhzpvv5x/app.bsky.feed.generator/aaacdps7yadba"
    follow_from_feed_generator(client, feed_generator_uri, max_to_follow=5, preferred_languages="en-US")
    log_activity("Followed authors from feed")

def resize_images_with_log():
    resize_all_images_in_folder(folder_path="images", target_size_mb=1)
    log_activity("Resized images to be under 1 MB")

# Schedule tasks
schedule.every().day.at("08:00").do(post_image_with_log)  # 8:00 AM
schedule.every().day.at("08:05").do(like_posts_with_log)  # 8:05 AM
schedule.every().day.at("08:10").do(follow_with_log)      # 8:10 AM
schedule.every().day.at("20:00").do(post_text_with_log)   # 8:00 PM

print("All tasks have been scheduled.")
wait_and_run()  # Keep the scheduler running
