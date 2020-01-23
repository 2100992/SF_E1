import random

from collections import defaultdict


class Round:
    '''class containing most of the game's logic "gallows"'''

    def __init__(self, wordset, max_unlucky_attempts=4):
        self.word = random.choice(wordset).upper()
        self.named_letters = defaultdict(int)
        self.max_unlucky_attempts = max_unlucky_attempts

    @property
    def hint(self):
        '''method calculates a hint depending on the letters already used
        returns result like property thanks to decorator
        '''
        
        hint = ''
        for l in self.word:
            if self.named_letters[l]:
                hint += f" {l}"
            else:
                hint += ' _'
        return hint.lstrip()

    @property
    def penalty_points(self):
        pp = 0
        for k, v in self.named_letters.items():
            if k not in self.word:
                pp += v
        return pp

    @property
    def game_over(self):
        if self.penalty_points > self.max_unlucky_attempts:
            return True
        return False

    @property
    def win(self):
        if '_' not in self.hint and not self.game_over:
            return True
        return False

    def set_letter(self, letters):
        for l in letters:
            self.named_letters[l.upper()] += 1

    def __str__(self):
        if self.game_over:
            return f"\n\nВы проиграли! \n Было загадано слово - {self.word} \n Отгаданы следующие буквы - {self.hint}. \n Штрафных баллов - {self.penalty_points}!\n\n"
        elif self.win:
            return f"\n\n{self.hint}\nВы победили!!!\n\n"
        return f"\nПродолжаем разговор! \n Угаданы следующие буквы - {self.hint}. \n Штрафных баллов - {self.penalty_points}!\n\n"
