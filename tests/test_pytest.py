import pytest

from gallows import Round

WORD_SET = ['testing']
test_round = Round(WORD_SET)

letters_sets = [
    '',
    't',
    'er',
    'stingy',
    'qwertyuiop',
    ]

hints = [
    '_ _ _ _ _ _ _',
    'T _ _ T _ _ _',
    'T E _ T _ _ _',
    'T E S T I N G',
    'T E S T I N G',
]

penalty_points = [
    0,
    0,
    1,
    2,
    9
]

wins = [
    False,
    False,
    False,
    True,
    False,
]

game_over = [
    False,
    False,
    False,
    False,
    True,
]

messages = [
    'Продолжаем разговор!',
    'Продолжаем разговор!',
    'Продолжаем разговор!',
    'Вы победили!',
    'Вы проиграли',
]