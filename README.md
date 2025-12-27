# Webhook-cli
An incredibly simple Linux cli tool to send messages to discord webhooks 

## Dependencies
- Make
- Python

## Installation

```sh
git clone https://github.com/icaruuuuuu/webhook-cli
cd webhook-cli
make install
```

## Usage
Webhook-cli takes two arguments: a message to be sent and a webhook URL.

Example 1:
`webhook-cli -m "This message was sent through webhook-cli" https://your-webhook-url`

Alternatively, you can send a .md file if your message is too complex to type in the cli

Example 2:
`webhook-cli -f message.md https://your-webhook-url`

