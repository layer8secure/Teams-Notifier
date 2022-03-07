![Layer-8-Logo-Wide](https://user-images.githubusercontent.com/8293038/96061566-93d8af00-0e61-11eb-8b84-3fd207290be2.png)
# Teams Notifier Plugin
An [Empire](https://github.com/BC-SECURITY/Empire) plugin that integrates Microsoft Teams notifications into Empire.

### Installation
Pre Reqs:
- Empire >=4.1.0

1. Add teams-notifier.py to Empire/empire/server/plugins
2. rename to have a .plugin extension
3. `sudo poetry add pymsteams`
4. Launch Empire Server

### Usage
1. create a listener
2. activate the plugin with `useplugin teams-notifier`
3. set to enabled
4. save in the webhook created in the teams channel of your choosing
5. Run the plugin with `execute`

### Adding a Web Hook
Using Teams Add a webhook in the target channel for notifications
https://dev.outlook.com/Connectors/GetStarted#creating-messages-through-office-365-connectors-in-microsoft-teams
https://dev.outlook.com/connectors/reference

### About
Built to allow for Empire to send a notification to Microsoft Teams upon successful agent connection.

Thank you to the BC Security team for helping especially [@vinnybod](https://github.com/vinnybod)!

### Author
- [Matthew Nickerson](https://github.com/mwnickerson) - Security Consultant at [Layer 8 Security](https://layer8security.com)

### Roadmap
- Add additional notifications for different agent events (disconnect, task compeletion, etc)
- Ability to interact with the Agent through the Teams channel
- Beautify the messages and colour codify when adding new event types

For additional feature requests please submit an [issue](https://github.com/layer8secure/Teams-Notifier/issues/new) and add the `enhancement` tag.

### License
[MIT License](https://opensource.org/licenses/MIT)
