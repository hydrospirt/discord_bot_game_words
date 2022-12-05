# Игра в слова 0.1

def find_words(file='RUS.txt'):
    try:
        word = open('RUS.txt', 'r')
        words = []
        for i in word:
            words.append(i)
    except Exception as err:
        print(err)
        return None
    finally:
        word.close()
        return [line.rstrip() for line in words]


def get_word(words):
    normilize_word = words.strip().lower()[1:]
    if normilize_word[-1] in ('ь', 'ъ'):
        normilize_word = normilize_word.strip().lower()[:-1]
    if is_correct_words(normilize_word):
        if (get_word.previous_word != '' and
           normilize_word[0] != get_word.previous_word[-1]):
            return 'Слово должно начинаться {0}'.format(
                get_word.previous_word[-1]
                )

        if normilize_word not in words_already_named:
            words_already_named.add(normilize_word)
            last_letter_word = normilize_word.capitalize()[-1]
            return f'Следующее слово на {last_letter_word}'
        else:
            return 'Слово уже было. Повторите попытку'
    else:
        return 'Некорректное название слова. Повторите попытку'


get_word.previous_word = ''


def is_correct_words(word):
    return word[-1].isalpha()


words_know = find_words()
words_already_named = set()

# Функция для бота дискорд
# async def on_message(message):
#   channel = message.channel
#   if message.author == bot.user:
#     return
#   if message.content.startswith('+'):
#     response = get_word(message.content)
#     await message.channel.send(response)