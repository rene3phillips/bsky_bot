# Content List: Each item is a dictionary with text and an image path (JSON)
CONTENT_LIST = [
    {"text": "Blockbuster nights = bonding time. What was your *go-to rental*? 🎥📼 #90sMovies", "image_path": "images/blockbuster.jpg"},
    {"text": "Remember when we all wanted to 'Be Like Mike'? 🏀 What's your favorite 90s sports moment? 🌟 #90sReplay", "image_path": "images/michael_jordan.jpeg"},
    {"text": "Goosebumps or Animorphs? Choose your childhood obsession. 📚🐾 #90sBooks", "image_path": "images/goosebumps.png"},
    {"text": "PS1 startup sound = Instant nostalgia. 🔊 Agree or agree? 📀 #RetroGaming", "image_path": "images/playstation.webp"},
    {"text": "Cowabunga! Who’s your favorite Ninja Turtle? 🥋🍕 #90sCartoons", "image_path": "images/ninja_turtles.png"},
    {"text": "Slip dresses, chokers, and butterfly clips—what 90s trend should make a comeback? 🦋 #90sStyle", "image_path": "images/choker.jpg"},
    {"text": "Tony Hawk’s Pro Skater made us ALL skaters. What’s your top move? 🚴‍♂️ #90sGames", "image_path": "images/tony_hawk.jpg"},
    {"text": "Pokémon Red or Blue—where did your journey begin? 🔥💧⚡ #KantoForever", "image_path": "images/pokemon_red.jpg"},
    {"text": "The Matrix made us all believe in leather jackets and tiny sunglasses. 🕶️ #90sMovies", "image_path": "images/matrix.jpg"},
    {"text": "Blowing on cartridges = gamer magic. What was your go-to 90s game? 🎮 #RetroGaming", "image_path": "images/nes_cartridge.jpeg"},
    {"text": "Choose your fighter: Street Fighter or Mortal Kombat? Fatality or Hadouken? 🕹️ #90sArcade", "image_path": "images/mortal_kombat.png"},
    {"text": "Clippy was the ultimate 90s sidekick. Where’s he now? 🖱️ #MicrosoftMemories", "image_path": "images/clippy.png"},
    {"text": "'BRB, gotta check my pager.' What was your first tech gadget? 📟 #90sTech", "image_path": "images/pager.png"}
]

# Initialize global index for tracking current content
current_image_index = 0

def post_image(client):
    """Post the next item in the CONTENT_LIST sequentially."""
    global current_image_index

    try:
        # Get the current content
        content = CONTENT_LIST[current_image_index]
        text = content["text"]
        image_path = content["image_path"]

        # Open the image and send the post
        with open(image_path, 'rb') as f:
            img_data = f.read()
        client.send_image(text=text, image=img_data, image_alt='90s Content')
        print(f"Posted content: {text}")

        # Update the index and reset if we've reached the end of the list
        current_image_index = (current_image_index + 1) % len(CONTENT_LIST)

    except Exception as e:
        print("An error occurred while posting content:", e)

