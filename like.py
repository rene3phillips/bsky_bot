import time  # Import the time module to add delays between actions

def like_recent_posts(client):
    try:
        # Retrieve timeline data with a limit of 10 posts
        data = client.get_timeline(cursor='', limit=10)  # Fetch the timeline data
        feed = data.feed  # List of posts from the timeline

        # Iterate over each post in the feed
        for feed_post in feed:
            post = feed_post.post  # Get the individual post object
            uri = getattr(post, 'uri', None)  # Retrieve the URI of the post, or None if it doesn't exist
            cid = getattr(post, 'cid', None)  # Retrieve the CID (content ID) of the post, or None if it doesn't exist

            # Check if both URI and CID exist
            if uri and cid:
                time.sleep(5)  # Pause for 5 seconds before liking the next post to avoid spamming
                client.like(uri=uri, cid=cid)  # Like the post using the client
                print(f"Liked post with URI: {uri} and CID: {cid}")  # Print confirmation message
            else:
                print("Skipping post with missing URI or CID.")  # Skip posts that are missing required data
    except Exception as e:
        print("An error occurred while liking posts:", e)  # Catch any exceptions and print an error message


