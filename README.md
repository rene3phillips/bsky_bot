
# Bsky Bot

A bot designed to interact with the Bluesky social network (Bsky) using the AT Protocol. This bot performs various automated tasks to enhance the user experience and provide unique functionalities.

---

## Features
- Automates posts, likes, and follows.  
- Interacts with the AT Protocol API for seamless integration.  
- Provides customizable content.  

---

## Prerequisites

Before you begin, ensure you have the following installed:  

1. **Python 3.13 or higher**  
2. **pip** for managing Python packages  

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/rene3phillips/bsky_bot.git  
   cd bsky_bot  
   ```

2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```

3. Set up your environment variables:  
   - Create a `.env` file in the root directory.  
   - Add the following:  
     ```
     ATPROTO_USERNAME=your_bsky_email  
     ATPROTO_PASSWORD=your_bsky_password  
     ```
---

## Customizing Posts
Before running the bot, you can edit the posts in the Python files. Each file corresponds to a specific part of the bot's functionality:  

- Edit `main.py` to change the time of posts and the feed generator URI.    
- Edit `data/post_image.json` to modify image post content.  
- Edit `data/post_text.json` to change text post content.  
- Place your own images in the `images` folder.  

Make sure to save the changes after editing these files.

---

## Running the Bot

1. Open the command prompt (or terminal on Mac).  

2. Navigate to the project directory:  
   ```bash
   cd path\to\bsky_bot  
   ```
   Replace `path\to\bsky_bot` with the actual path to your bot folder.  

3. Run the bot:  
   ```bash
   main.py  
   ```
   The bot will run with the updated content from the files you edited.

---

## Current Use

I am currently using this bot for an online social media account related to **90s Replay**, a future business idea that my son and I want to create. The account posts a lot of 90s nostalgia content, celebrating the era with fun and engaging posts. 

If you’re interested, you can follow the account to see the bot in action or simply enjoy some 90s memories: **@90sReplay** on Bluesky.

---

## Disclaimer

This bot is for educational purposes only. Please use responsibly and ensure compliance with Bluesky's terms of service. I independently created this project, and it is not affiliated with Bluesky in anyway.

---

## Contact

If you have questions or need support, feel free to reach out:

- **Email**: rene3phillips@gmail.com  
- **GitHub**: https://github.com/rene3phillips  

Happy coding!

