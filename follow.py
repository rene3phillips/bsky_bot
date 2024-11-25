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
        # Fetch feed data from the generator URI using the Bluesky API
        data = client.app.bsky.feed.get_feed({
            'feed': generator_uri,  # Feed generator URI
            'limit': 30,            # Limit the number of posts to fetch
        }, headers={'Accept-Language': preferred_languages})

        feed = data.feed  # Extract the feed data
        next_page = data.cursor  # Pagination cursor (if needed)

        # Fetch metadata about the feed generator using get_feed_generator method
        feed_metadata = client.app.bsky.feed.get_feed_generator({
            'feed': generator_uri
        })

        # Extract and print feed generator metadata
        view = feed_metadata.view
        print(f"Feed Generator Name: {view.display_name}")
        print(f"Creator DID: {view.creator}")
        print(f"Avatar URL: {view.avatar}")
        print(f"Like Count: {view.like_count}")

        # Initialize a counter for how many people to follow
        count = 0

        # Loop over each post in the feed
        for feed_post in feed:
            if count >= max_to_follow:
                break  # Stop once we've followed the desired number of people

            # Extract the 'did' (Document Identifier) of the author
            post = feed_post.post
            if hasattr(post, 'author') and hasattr(post.author, 'did'):
                author_did = post.author.did

                # Follow the author (if not already followed)
                try:
                    time.sleep(5)  # Add a delay to avoid hitting rate limits
                    client.follow(author_did)
                    print(f"Followed user: {author_did}")
                    count += 1
                except Exception as e:
                    print(f"Failed to follow user {author_did}: {e}")

        if count == 0:
            print("No users found to follow.")
        else:
            print(f"Followed {count} users from the feed generator.")

    except Exception as e:
        print("An error occurred:", e)


