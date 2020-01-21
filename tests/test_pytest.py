import pytest

from gallows import Round

WORD_SET = ['testing']
new_round = Round(WORD_SET)

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

games_over = [
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

@pytest.fixture(params=range(5))
def iter(request):
    return request.param


def test_round(iter):
    new_round.set_letter(letters_sets[iter])
    assert new_round.hint == hints[iter]
    assert new_round.penalty_points == penalty_points[iter]
    assert new_round.win == wins[iter]
    assert new_round.game_over == games_over[iter]
    assert new_round.__str__() == messages[iter]
