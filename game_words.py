import random

from russian import words

words_already_named = ['лл']
pre_word = ''
happy_msg = (
    'Отлично, такое слово есть!',
    'Вау, у нас тут знаток слов!',
    'Может быть хватит!? Отгадывать мои слова :)',
    'О как великолепно, когда слово есть!:)',
    'И-и-и-и.....',
    'Барабанная дробь *_*_*_ и:',
    'Н-у-у-у, это правильное слово!',
    'Угадайка-отгадайка!',
    'Белиссимо-словисимо! Правильно :)',
    'Ты-ы-ы-ы просто чудо!^)'
)


def happy_say(word: str, words=words) -> str:
    '''Сообщения для пользователя'''
    player_word = word.rstrip().lower()
    if words.get(player_word):
        return random.choice(happy_msg)


def check_word(word: str, words=words) -> str:
    '''Игра в слова'''
    player_word = word.rstrip().lower()
    if words.get(player_word):
        if player_word[-1] in ('ь', 'ъ') and len(player_word) > 3:
            if player_word not in words_already_named:
                words_already_named.append(player_word)
                words_already_named.append(player_word[:-1])
                last_letter = player_word.upper()[-2]
                return 'Следующее слово должно начинаться на ' + '"' + last_letter + '"'
        if words_already_named and player_word[-1] not in ('ь', 'ъ'):
            if player_word[0] != words_already_named[-1][-1]:
                return 'Но-но, по-легче! Слово должно начинаться букву "{0}"!'.format(words_already_named[-1][-1].upper())
            else:
                if player_word not in words_already_named:
                    words_already_named.append(player_word)
                    last_letter = player_word.upper()[-1]
                    return 'Следующее слово должно начинаться на ' + '"' + last_letter + '"'
                else:
                    return 'Слово уже было. Повторите попытку'
    else:
        return (
            f'Сам ты "{player_word.upper()}".'
            f'Такого слова нет в моем словаре, придумай другое!')
