import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initialize a Web API client
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

def fetch_channel_history(channel_id):
    try:
        result = client.conversations_history(channel=channel_id)
        return result['messages']
    except SlackApiError as e:
        print(f"Error fetching conversations: {e}")
        return []

def save_to_text(channel_id, messages):
    with open(f"{channel_id}_history.txt", "w") as file:
        for message in messages:
            file.write(f"{message['ts']}: {message['text']}\n")

if __name__ == "__main__":
    # Replace 'C1234567890' with your channel ID
    channel_id = 'C1234567890'
    messages = fetch_channel_history(channel_id)
    save_to_text(channel_id, messages)
