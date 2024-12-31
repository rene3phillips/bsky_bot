from dotenv import load_dotenv # reads environment variables from .env file
import os # for interacting with the operating system
from atproto import Client # used to interact with AT Protocol
import schedule # used to schedule tasks
import time # used for sleep function
from datetime import datetime # used to log current date and time

# Load environment variables from the .env file
load_dotenv()

# Retrieve username and password from environment variables
username = os.getenv('ATPROTO_USERNAME')  # Get the username from environment variables
password = os.getenv('ATPROTO_PASSWORD')  # Get the password from environment variables

# Check if the username and password are set in the environment variables
if not username or not password:
    raise ValueError("Environment variables for username or password are not set.")

# Initialize the AT Protocol client
client = Client()

# Login to the client using the credentials
client.login(username, password)

# Function to return a logged-in client object
def authenticate():
    return client  # Returns the authenticated client instance

# Logs the activity with the current date and time
def log_activity(activity):
    current_time = datetime.now().strftime("%m/%d/%y %I:%M %p")  # Get the current time in desired format (e.g., 12/30/24 12:19 PM)
    print(f"{current_time} - {activity}")  # Print the log message with timestamp

# Run scheduled tasks in a loop
def wait_and_run():
    print("Starting task scheduler...")  # Print a message to indicate the scheduler has started
    # Infinite loop to keep running scheduled tasks
    while True:
        schedule.run_pending()  # Run any pending tasks that are scheduled
        time.sleep(1)  # Sleep for 1 second before checking again
