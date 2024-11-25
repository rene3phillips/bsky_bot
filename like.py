import time

def like_recent_posts(client):
    """Like recent posts on the timeline."""
    try:
        # Retrieve timeline data with a limit of 10 posts
        data = client.get_timeline(cursor='', limit=10)
        feed = data.feed  # List of posts from the timeline

        for feed_post in feed:
            post = feed_post.post
            uri = getattr(post, 'uri', None)
            cid = getattr(post, 'cid', None)

            if uri and cid:
                time.sleep(5)
                client.like(uri=uri, cid=cid)
                print(f"Liked post with URI: {uri} and CID: {cid}")
            else:
                print("Skipping post with missing URI or CID.")
    except Exception as e:
        print("An error occurred while liking posts:", e)

