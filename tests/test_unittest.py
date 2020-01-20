import unittest

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


class TestRound(unittest.TestCase):
    def test_round(self):
        for i, l_set in enumerate(letters_sets):
            test_round.set_letter(l_set)
            self.assertEqual(test_round.hint, hints[i])
            self.assertEqual(test_round.penalty_points, penalty_points[i])
            self.assertEqual(test_round.win, wins[i])
            self.assertEqual(test_round.game_over, game_over[i])


# class TestCreateNewRound(unittest.TestCase):


import sys

if __name__ == '__main__':
    unittest.main()