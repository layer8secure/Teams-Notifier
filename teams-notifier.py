# Microsoft Teams Notifier Plugin
# A Plugin to send a notification to teams when an agent connects
# Needs to have a teams webhook for it to work
# Consult the microsoft doumentation on how to create a webhook
# https://dev.outlook.com/Connectors/GetStarted#creating-messages-through-office-365-connectors-in-microsoft-teams
# TODO: Beautfiy the Teams messages with colours
# TODO: Add more notifications
# TODO: Receive commands from teams?

from __future__ import print_function

# Empire imports
from empire.server.common.hooks import hooks
from empire.server.common.plugins import Plugin
from empire.server.database import models

# Teams integration imports
import pymsteams

# Must be named plugin
class Plugin(Plugin):

    def onLoad(self):
        self.info = {
                        # Plugin Name, at the moment this much match the do_ command
                        'Name': 'teams-notifier',

                        'Author': ['b0than'],

                        'Description': ('Sends a message to Teams on agent connect'),

                        # Software and tools that from the MITRE ATT&CK framework (https://attack.mitre.org/software/)
                        'Software': '',

                        # Techniques that from the MITRE ATT&CK framework (https://attack.mitre.org/techniques/enterprise/)
                        'Techniques': [],

                        # List of any references/other comments
                        'Comments': [
                            'Uses the Teams Webhook integration to generate messages on Agent connection',
                            'Create a webhook in Teams in order for the plugin to work',
                            'See Microsoft Documentation on creating a webhook',

                        ]
                    },

        self.options = {
            'teams_webhook': {
                'Description': 'Webhook URL',
                'Required': True,
                'Value': ''
            },
            'enabled': {
                'Description': 'Turn the plugin on or off',
                'Required': True,
                'Value': 'False',
                'SuggestedValues': [
                    'True',
                    'False'
                ],
                'Strict': True
            }
        }

    def execute(self, command):
        """
        parses commands from the API
        """
        if command['enabled'] == 'False':
            hooks.unregister_hook('teams-notifier', hooks.AFTER_AGENT_CHECKIN_HOOK)
            self.main_menu.plugin_socketio_messages(self.info[0]['Name'], f'[*] Teams Notifier Plugin turned off')
        else:
            self.options['teams_webhook']['Value'] = command['teams_webhook']
            hooks.register_hook(hooks.AFTER_AGENT_CHECKIN_HOOK, 'teams-notifier', self.teams_notify)
            self.main_menu.plugin_socketio_message(self.info[0]['Name'], f'[*]Teams Notifier turned on')

    def register(self, mainMenu):
        """
        Any modifications to the main menu go here
        """
        self.main_menu = mainMenu

    def teams_notify(self, agent: models.Agent):
        teams_message = pymsteams.connectorcard(self.options['teams_webhook']['Value'])
        teams_message.text(f"New Agent Check In {agent.session_id} on listener {agent.listener}")
        teams_message.send()

    def shutdown(self):
        """
        Kills additional process that were spawned
        """
        pass



