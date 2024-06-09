import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize a Web API client
client = WebClient(token=os.getenv('SLACK_BOT_TOKEN'))

def fetch_channel_history(channel_id):
    messages = []
    try:
        result = client.conversations_history(channel=channel_id, limit=100)
        messages.extend(result['messages'])
        while result['has_more']:
            result = client.conversations_history(channel=channel_id, limit=100, cursor=result['response_metadata']['next_cursor'])
            messages.extend(result['messages'])
    except SlackApiError as e:
        print(f"Error fetching conversations: {e}")
    return messages

def save_to_text(channel_id, messages):
    with open(f"{channel_id}_history.txt", "w") as file:
        for message in messages:
            file.write(f"{message['ts']}: {message['text']}\n")

if __name__ == "__main__":
    # Replace 'C1234567890' with your channel ID
    channel_id = 'C05KYDD52BT'
    messages = fetch_channel_history(channel_id)
    save_to_text(channel_id, messages)
