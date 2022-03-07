# Teams Notifier Plugin
The Teams Notifier plugin is designed to use webhooks in order to generate alerts sent to a teams channel when an agent checks in 

## Install
Pre Reqs:
- Empire >=4.1.0

1. Add teams-notifier.py to Empire/empire/server/plugins
2. rename to have a .plugin extension
3. `sudo poetry add pymsteams`
4. Launch Empire Server

## Usage
1. create a listener
2. activate the plugin with `useplugin teams-notifier`
3. set to enabled
4. save in the webhook created in the teams channel of your choosing
5. Run the plugin with `execute`

## Adding a Web Hook
Using Teams Add a webhook in the target channel for notifications
https://dev.outlook.com/Connectors/GetStarted#creating-messages-through-office-365-connectors-in-microsoft-teams
https://dev.outlook.com/connectors/reference
