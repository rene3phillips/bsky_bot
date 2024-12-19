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
2. **pip3** for managing Python packages  

---

## Installation

1. Clone the repository:  
   git clone https://github.com/rene3phillips/bsky_bot.git  
   cd bsky_bot  

2. Install the required dependencies:  
   pip3 install -r requirements.txt  

3. Set up your environment variables:  
   - Create a `.env` file in the root directory.  
   - Add the following:  
     ATPROTO_USERNAME=your_bsky_email  
     ATPROTO_PASSWORD=your_bsky_password  
---

## Customizing Posts
Before running the bot, you can edit the posts in the Python files. Each file corresponds to a specific part of the bot's functionality:  

Edit main.py to change the time of posts.    
Edit post_image.py to modify image post content.  
Edit post_text.py to change text post content.  
Make sure to save the changes after editing these files.

## Running the Bot
Open the command prompt (or terminal on Mac).  

Navigate to the project directory:  
cd path\to\bsky_bot  
Replace path\to\bsky-bot with the actual path to your bot folder.  

## Run the bot:  
python main.py  
The bot will run with the updated content from the files you edited.  

---

## Disclaimer

This bot is for educational purposes only. Please use responsibly and ensure compliance with Bluesky's terms of service.

---

## Contact

If you have questions or need support, feel free to reach out:

- **Email**: rene3phillips@gmail.com
- **GitHub**: https://github.com/rene3phillips

Happy coding!

