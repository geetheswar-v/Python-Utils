import random
import json
import numpy as np
import nltk
import sys

sys.path.append('/home/geetheswar/Documents/projects/ChatMate/')

from nltk.stem import WordNetLemmatizer
from helper import *
from keras.models import load_model
from weather.helper import get_weather
from calculator.evaluator.evaluator import Evaluator
import pickle

nltk.download("punkt")
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('/home/geetheswar/Documents/projects/ChatMate/chatmate/files/data.json').read())

words = pickle.load(open('/home/geetheswar/Documents/projects/ChatMate/chatmate/files/words.pkl', 'rb'))
tags = pickle.load(open('/home/geetheswar/Documents/projects/ChatMate/chatmate/files/tags.pkl', 'rb'))
model = load_model('/home/geetheswar/Documents/projects/ChatMate/chatmate/files/model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def get_predicted_intent(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    res = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    res.sort(key=lambda x: x[1], reverse=True)
    predicts = []
    for r in res:
        predicts.append({'intent': tags[r[0]], 'probability': str(r[1])})
    return predicts


def get_response(intents_list, intents_json, question):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    res = "I didn't understand your question"
    for i in list_of_intents:
        if tag == 'iit_pkd':
            name = get_name(question)
            res = get_details(name)
            break
        if tag == 'time':
            res = get_timeline()
            break
        if tag == 'stocks':
            res = get_stocks(question)
            break
        if tag == 'calculator':
            expr = get_expression(question)
            evaluator = Evaluator()
            result = evaluator.evaluate(expr)
            res = f'The answer for {expr} is {result}'
            break
        if tag == 'weather':
            city = get_city(question)
            res = get_weather(city)
            break
        if i['tag'] == tag:
            res = random.choice(i['responses'])
            break
    return res


def get_message(sentence):
    predicted_list = get_predicted_intent(sentence)
    return get_response(predicted_list, intents, sentence)

if __name__ == '__main__':
    while True:
        message = input("")
        if message == "":
            break
        ints = get_predicted_intent(message)
        ress = get_response(ints, intents, message)
        print(ress)
