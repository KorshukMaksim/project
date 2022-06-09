
import re  # Regular Expressions
import nltk  # Natural Language Toolkit


def filter_text(text):
    text = text.lower()
    pattern = r'[^\w\s]'
    text = re.sub(pattern, "", text)
    return text


# На вход: два текста, на выход: boolean(True, False)
# Функция isMatch вернет True, если тексты совпадают или False иначе
def is_match(text1, text2):
    # text1 = text1.lower()  # Приводим к нижнему регистру ("ПрИвет" => "привет")
    # text2 = text2.lower()

    # # Удаление знаков препинания
    # # = Удалить все кроме букв и пробелов
    # pattern = r'[^\w\s]'
    # text1 = re.sub(pattern, "", text1) # Делать замену символов в строке
    # text2 = re.sub(pattern, "", text2)
    text1 = filter_text(text1)
    text2 = filter_text(text2)

    if len(text1) == 0 or len(text2) == 0:
        return False

    # Проверить что одна фраза является частью другой

    # Text1 содержит text2
    if text1.find(text2) != -1:
        return True

    # Text2 содержит text1
    if text2.find(text1) != -1:
        return True

    # Расстояние Левенштейна (edit distance = расстояние редактирования)
    distance = nltk.edit_distance(text1, text2)  # Кол-во символов 0...Inf
    length = (len(text1) + len(text2)) / 2  # Средняя длина двух текстов
    score = distance / length  # 0...1

    return score < 0.6
# Сколько символов нужно отредактировать "мама" = (1) => "мамы"
nltk.edit_distance("Привет братан", "Превед бротан")
# 0, 1, 2, 3...
# 0 ... 0.3 ... 0.5 ... 1

import random

# Намерения = Intents
# Поздароваться, спросить как дела, спросить имя или чем занимаешься
# Заказать пиццу, отменить заказ, добавить больше сыра

# Конфигурация бота
BOT_CONFIG = {
    # Все намерения которые поддерживает наш бот
    "intents": {
        "hello": {
            "examples" : ["Привет", "Здарова", "Йо", "Приветос", "Хеллоу"],
            "responses": ["Здравстсвтсвтвтвуй человек", "И тебе не хворать", "Здоровее видали"],
        },
        "how_are_you": {
            "examples" : ["Как дела", "Чо каво", "Как поживаешь"],
            "responses": ["Маюсь Фигней", "Веду интенсивы", "Учу Пайтон"],
        }
    },
    # Фразы когда бот не может ответить
    "failure_phrases": ["Даже не знаю что сказать", "Поставлен в тупик", "Перефразируйте, я всего лишь бот"],
}

def printAnswer(text, examples, responses):
  for example in examples:  # Для каждого элемента списка examples
    if is_match(text, example):  # Если пример совпадает с текстом пользователя
      print(random.choice(responses))  # Выводим на экран случайный элемент списка responses

text = input()

# Для каждого намерения, пытаемся напечатать ответ
for intent in BOT_CONFIG["intents"].values():
    printAnswer(text, intent["examples"], intent["responses"])

import json

config_file = open("D:\Big_bot_config.json", "r")
BIG_CONFIG = json.load(config_file)

BIG_CONFIG.keys()
len(BIG_CONFIG["intents"])

X = [] # Фразы
y = [] # Намерения

# Собираем фразы и интенты из BIG_CONFIG в X,y
for name, intent in BIG_CONFIG["intents"].items():
  for example in intent["examples"]:
    X.append(example)
    y.append(name)
  for example in intent["responses"]:
    X.append(example)
    y.append(name)

len(X)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer() # Можно указать настройки
vectorizer.fit(X) # Учится вот эти конкретные тексты превращать в числа

arr = vectorizer.transform(["друг друг друг друг привет"]).toarray()[0]
for a in arr:
  if a!=0:
    print(a, end=',')

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

model = RandomForestClassifier() # Настройки
vecX = vectorizer.transform(X) # Преобразуем тексты в вектора
model.fit(vecX, y)  # Обучаем модель
model.score(vecX, y)

import random
from random import choice


def get_intent_ml(text):
    vec_text = vectorizer.transform([text])
    intent = model.predict(vec_text)[0]
    # ToDo: выдавать ответ только если модель уверена в нем
    return intent