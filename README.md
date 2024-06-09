
# Slack Channel History Exporter

## Purpose

This repository contains a Python script to export the entire message history of a specified Slack channel to a text file. The script leverages the Slack API to fetch and save the channel history, making it easy to archive or analyze the conversations from your Slack workspace.

## Setup

### Step 1: Create a Slack App

1. Go to the [Slack API](https://api.slack.com/) site.
2. Click on "Create an App" and choose "From scratch".
3. Name your app and select the workspace where you want to install it.

### Step 2: Add Permissions

1. Navigate to the "OAuth & Permissions" section of your app.
2. Add the following Bot Token Scopes:
   - `channels:history`
   - `groups:history`
   - `im:history`
   - `mpim:history`
   - `channels:read`
   - `groups:read`
   - `im:read`
   - `mpim:read`

### Step 3: Install the App

1. Install the app to your workspace by clicking "Install App to Workspace".
2. Authorize the app for your workspace.

### Step 4: Get the Access Token

1. Copy the Bot User OAuth Token from the "OAuth & Permissions" section.

## Usage

### Step 1: Install Dependencies

Ensure you have Python installed, then install the necessary packages:

\`\`\`bash
pip install slack_sdk python-dotenv
\`\`\`

### Step 2: Set Up Environment Variables

Create a \`.env\` file in the same directory as your script and add the following line:

\`\`\`env
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
\`\`\`

### Step 3: Configure and Run the Script

1. Open the \`export_slack_history.py\` file.
2. Replace \`'C1234567890'\` with the ID of the Slack channel you wish to export.
3. Run the script:

\`\`\`bash
python export_slack_history.py
\`\`\`

### Step 4: View the Exported History

The script will create a text file named \`<channel_id>_history.txt\` containing the message history of the specified Slack channel.

## Script Details

The script performs the following steps:

1. Loads environment variables from the \`.env\` file.
2. Initializes the Slack Web API client using the provided bot token.
3. Fetches the message history of the specified Slack channel, handling pagination if necessary.
4. Saves the messages to a text file in the format \`<timestamp>: <message>\`.

## Handling Pagination

The script automatically handles pagination. If the channel has a large number of messages, it will iterate through the pages using the \`cursor\` parameter provided by Slack's API to fetch all messages.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
