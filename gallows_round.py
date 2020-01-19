import random

from collections import defaultdict


class Round:
    word = None
    unlucky_attempts = 4

    def __init__(self, wordset):
        self.word = random.choice(wordset).upper()
        self.named_letters = defaultdict(int)

    @property
    def hint(self):
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
        if self.penalty_points > self.unlucky_attempts:
            return True
        else:
            return False

    @property
    def win(self):
        if '_' not in self.hint and not self.game_over:
            return True
        else:
            return False

    def set_letter(self, letters):
        for l in letters:
            self.named_letters[l.upper()] += 1

    def __str__(self):
        if self.game_over:
            return f"\n\nИгра проиграна! \n Было загадано слово - {self.word} \n Отгаданы следующие буквы - {self.hint}. \n Штрафных баллов - {self.penalty_points}!\n\n"
        elif self.win:
            return f"\n\n{self.hint}\nВы победили!!!\n\n"
        else:
            return f"\nПродолжаем разговор! \n Угаданы следующие буквы - {self.hint}. \n Штрафных баллов - {self.penalty_points}!\n\n"
