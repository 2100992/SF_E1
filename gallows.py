import random

from gallows_round import Round

from h import WORDS_SET


def gallows():
    new_round = Round(WORDS_SET)
    print('\n\nЯ загадал слово!\n')
    # print(new_round.word)
    print(f'Подсказка - {new_round.hint}')
    while not new_round.win and not new_round.game_over:
        new_letter = input('Назовите вашу букву\n\n')
        new_round.set_letter(new_letter)
        print(new_round)


def main():
    lets_go = input('\n\nСыграем в игру "Висилица"?\n')
    
    if lets_go.lower() in ['да', 'yes', 'y', 'д']:
        print('Поехали')
        gallows()

    else:
        print('\nПока пока!\n')


if __name__ == "__main__":
    main()
