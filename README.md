# Telegram bot for counting time to event. Hosted on Yandex Cloud Functions

## Env vars

`BOT_TOKEN` — Telegram bot token
`EVENT_DATETIME` — Date and time of event in the format `%d.%m.%Y %H:%M`. E.g. '08.10.2022 14:20')
`MESSAGE_PREFIX` — Prefix for telegram message that will be followed by date. E.g. 'Time until arrival: '
`MESSAGE_EVENT_PASSED` — Message to send in case the event has already passed. E.g. 'He already arrived'
`INLINE_TITLE` — Title for inline answer option. E.g. 'Get time until arrival'


## Deployment
1. Make sure that you have YC CLI installed and initialized: https://cloud.yandex.com/en/docs/cli/quickstart#install
2. If you haven't created a function yet, create it with the following command: 
```
yc serverless function create --name=<function name>
```
3. To upload the code and create a new version run the following command substituting <> to your values where necessary:
```
yc serverless function version create \
  --function-name=<function name> \
  --runtime python39 \
  --entrypoint index.handler \
  --memory 128m \
  --execution-timeout 3s \
  --source-path . \
  --environment 'BOT_TOKEN=<bot_token' \
  --environment 'EVENT_DATETIME=<event_datetime>' \
  --environment 'MESSAGE_PREFIX=<message_prefix>' \
  --environment 'MESSAGE_EVENT_PASSED=<message_event_passed>' \
  --environment 'INLINE_TITLE=<inline_title>'
```


Don't forget to enable inline mode in BotFather
