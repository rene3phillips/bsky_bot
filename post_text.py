# Content List
CONTENT_LIST = [
    {"text": "Lisa Frank’s bright designs were the ultimate vibe. Did you rock her folders in school? ✨ #90sStyle"},
    {"text": "'You wouldn’t download a car...' Those anti-piracy ads live rent-free in our heads. 😂 #RetroLaughs"},
    {"text": "Long car rides meant battling over the radio dial. What was your ultimate 90s road trip song? 🚗🎶 #90sMusic"},
    {"text": "Were you Team Airwalks or Team Doc Martens back in the day? 👟 #90sStyle"},
    {"text": "Custom Pokémon sprites were a badge of honor. Did you ever make one? 🎨 #PokémonNostalgia"},
    {"text": "AIM away messages were basically 90s poetry. What was your most iconic one? 💬🖥️ #RetroInternet"},
    {"text": "Crystal Pepsi was the clear choice for soda in the 90s. Did you ever try it? 🥤 #90sDrinks"},
    {"text": "LAN parties were proof you didn’t need Wi-Fi to game with friends. 🔌 #TechNostalgia"},
    {"text": "Warheads were the ultimate sour candy challenge. Sweet victory or too intense? 🍬 #RetroCandy"},
    {"text": "'I’ll be there for you...' If *Friends* wasn’t part of your week, what was? 🖤 #90sTV"},
    {"text": "Saturday mornings were a mix of sugary cereal and cartoons. What was your cereal of choice? 🥣📺 #90sSnacks"},
    {"text": "TRL was where music met chaos. Who topped your list of must-see artists? 🎵📺 #90sMusic"},
    {"text": "VHS tapes were rewind or bust. What was your most-watched movie? 📼 #RetroMedia"},
    {"text": "TGIF Fridays had the best shows and the best vibes. What was your go-to lineup? 📺 #90sTV"}
]

# Global index to track current content
current_index = 0

def post_text(client):
    """Post text from the CONTENT_LIST."""
    global current_index

    try:
        # Get the content to post
        text_content = CONTENT_LIST[current_index]["text"]
        
        # Send the post
        client.send_post(text=text_content)
        print(f"Successfully posted: {text_content}")

        # Update the index and reset if we've reached the end of the list
        current_index = (current_index + 1) % len(CONTENT_LIST)

    except Exception as e:
        print(f"Error posting content: {e}")

