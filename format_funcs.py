from typing import Union


def format_days(days: Union[int, float, str]) -> str:
    d = int(days) % 10
    if int(days) % 100 in {11, 12, 13, 14}:
        text = 'дней'
    elif d == 1:
        text = 'день'
    elif d in {2, 3, 4}:
        text = 'дня'
    else:
        text = 'дней'
    return f'{days} {text}'


def format_hours(hours: Union[int, float, str]) -> str:
    d = int(hours) % 10
    if int(hours) % 100 in {11, 12, 13, 14}:
        text = 'часов'
    elif d == 1:
        text = 'час'
    elif d in {2, 3, 4}:
        text = 'часа'
    else:
        text = 'часов'
    return f'{hours} {text}'


def format_minutes(minutes: Union[int, float, str]) -> str:
    d = int(minutes) % 10
    if int(minutes) % 100 in {11, 12, 13, 14}:
        text = 'минут'
    elif d == 1:
        text = 'минута'
    elif d in {2, 3, 4}:
        text = 'минуты'
    else:
        text = 'минут'
    return f'{minutes} {text}'
