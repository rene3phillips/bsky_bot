from dotenv import load_dotenv
import os
from atproto import Client
import schedule
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Retrieve username and password from environment variables
username = os.getenv('ATPROTO_USERNAME')
password = os.getenv('ATPROTO_PASSWORD')

if not username or not password:
    raise ValueError("Environment variables for username or password are not set.")

# Initialize the client
client = Client()
client.login(username, password)

def authenticate():
    """Return a logged-in client object."""
    return client

def log_activity(activity):
    """Logs the activity with the current timestamp."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - {activity}")

def wait_and_run():
    """Run scheduled tasks in a loop."""
    print("Starting task scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)
