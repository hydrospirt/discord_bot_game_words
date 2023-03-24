# discord_bot_game_words
## Игра в слова v 0.2

- Добавлен поиск по словарю
- Исправлены ошибки
- ✨Magic ✨

## Описание

- Игра для настоящих интеллектуалов, необходимо отгадывать слова.
- Словарь на 51 000 тысячу слов.


Пример: Было загадно слово "ЛОСЬ", значит следующее слово необходимо назвать на "С", игра игнорирует "Ь", "Ъ", потому что таких слов мало.

## Технологии

В этом проекте использовались такие технологии:

- Python 3.10


## Как добавить в discord bot


Добавьте импорты:

```sh
from game_words2 import *
from russian import words
```

Добавьте функции, пример:

```sh

  if message.content.startswith('+'):
    happy = happy_say(message.content[1:], words=words)
    await message.channel.send(happy)
  
  if message.content.startswith('+'):
    response = check_word(message.content[1:], words=words)
    await message.channel.send(response)
```


## Лицензия

BSD 3-Clause "New" or "Revised" License

**Бесплатное использование**

