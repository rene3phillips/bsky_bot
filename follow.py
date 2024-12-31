import time

def follow_from_feed_generator(client, generator_uri, max_to_follow=5, preferred_languages="en-US"):
    """
    Follow up to `max_to_follow` authors from a specific feed generator.

    Parameters:
        client: The authenticated Bluesky client object.
        generator_uri (str): The URI of the feed generator (e.g., at://<did>/app.bsky.feed.generator/<record_key>).
        max_to_follow (int): The maximum number of authors to follow.
        preferred_languages (str): The language preference for the response (default: "en-US").
    """
    try:
        # Fetch feed data from the specified generator URI
        data = client.app.bsky.feed.get_feed({
            'feed': generator_uri,  # Feed generator URI
            'limit': 30,            # Maximum number of posts to fetch in a single request
        }, headers={'Accept-Language': preferred_languages})  # Specify preferred language for responses

        feed = data.feed  # Extract the list of posts from the feed

        # Retrieve metadata about the feed generator
        feed_metadata = client.app.bsky.feed.get_feed_generator({
            'feed': generator_uri  # Provide the feed generator URI to fetch metadata
        })

        # Extract and display information about the feed generator
        view = feed_metadata.view
        print(f"Feed Generator Name: {view.display_name}")  # Name of the feed generator
        print(f"Creator DID: {view.creator}")  # Decentralized identifier (DID) of the generator creator
        print(f"Avatar URL: {view.avatar}")  # URL of the feed generator's avatar image
        print(f"Like Count: {view.like_count}")  # Number of likes for the feed generator

        # Initialize a counter to keep track of how many authors have been followed
        count = 0

        # Iterate over each post in the feed
        for feed_post in feed:
            if count >= max_to_follow:
                break  # Exit the loop once the maximum number of authors is followed

            # Extract the 'did' (Document Identifier) of the post's author
            post = feed_post.post
            if hasattr(post, 'author') and hasattr(post.author, 'did'):  # Ensure author and DID exist
                author_did = post.author.did  # Get the DID of the post's author

                # Attempt to follow the author if not already followed
                try:
                    time.sleep(5)  # Wait 5 seconds between follow actions to avoid rate limits
                    client.follow(author_did)  # Send follow request for the author
                    print(f"Followed user: {author_did}")  # Log successful follow
                    count += 1  # Increment the follow counter
                except Exception as e:
                    print(f"Failed to follow user {author_did}: {e}")  # Log failure and continue

        # Display results of the follow actions
        if count == 0:
            print("No users found to follow.")  # Indicate no authors were followed
        else:
            print(f"Followed {count} users from the feed generator.")  # Summarize the follow count

    except Exception as e:
        print("An error occurred:", e)  # Handle and log any exceptions during execution


