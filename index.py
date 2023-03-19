import os
import logging
import json
import time
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

import format_funcs as ff

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ANSWER_URL = f'https://api.telegram.org/bot{os.environ["BOT_TOKEN"]}/answerInlineQuery'
EVENT_DATETIME = datetime.strptime(os.environ['EVENT_DATETIME'], '%d.%m.%Y %H:%M').replace(tzinfo=ZoneInfo('Europe/Moscow'))
MESSAGE_PREFIX = os.environ['MESSAGE_PREFIX']
MESSAGE_EVENT_PASSED = os.environ['MESSAGE_EVENT_PASSED']
INLINE_TITLE = os.environ['INLINE_TITLE']


def construct_answer(data):
    now = datetime.now().astimezone(ZoneInfo('Europe/Moscow'))
    query_id = data['inline_query']['id']
    if EVENT_DATETIME <= now:
        result_text = MESSAGE_EVENT_PASSED
    else:
        diff = EVENT_DATETIME - now
        days = diff.days
        hours = diff.seconds // 60 // 60
        minutes = diff.seconds // 60 - (hours * 60)
        result_text = (
            MESSAGE_PREFIX +
            f' {ff.format_days(days)}, {ff.format_hours(hours)} и {ff.format_minutes(minutes)}'
        )
    result = {
        'inline_query_id': query_id,
        'cache_time': 1,
        'results': [
            {
                'type': 'article',
                'id': str(int(time.time())),
                'title': 'INLINE_TITLE',
                'input_message_content': {'message_text': result_text},
            }
        ]
    }
    return result


def handler(event, context):
    answer = construct_answer(json.loads(event['body']))
    logger.info(ANSWER_URL)
    logger.info(answer)
    r = requests.post(ANSWER_URL, json=answer)
    logger.info(r.content)
    return {
        'statusCode': 200,
        'body': 'ok',
    }
