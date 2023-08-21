import os
from slack_sdk.webhook import WebhookClient
from datetime import datetime

SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK', 'NotReadFromEnv')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL', 'NotReadFromEnv')
MY_NODE_NAME = os.environ.get('MY_NODE_NAME', 'NotReadFromEnv')
MY_POD_NAME = os.environ.get('MY_POD_NAME', 'NotReadFromEnv')
MY_TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

message = f"This CronJob was run on this shortlived pod: {MY_POD_NAME} At {MY_TIME} On Node: {MY_NODE_NAME} And Posted to: {SLACK_CHANNEL}"

print("The SLACK_CHANNEL is set to: ", os.environ.get('SLACK_CHANNEL'))
print("Message:", message)

slack_client = WebhookClient(SLACK_WEBHOOK)

response = slack_client.send(
    text = "message",
)