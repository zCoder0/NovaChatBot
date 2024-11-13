import pickle
import numpy as np
import spacy
import nltk
import json
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from tensorflow import keras
import re
class MyModel:

    def __init__(self):
        with open('BModels/ChatModel.pickle', 'rb') as file:
            self.model = pickle.load(file)
        
    def loadEncoder(self):
        with open('BModels/LabelEnoceder.pickle', 'rb') as file:
            self.encoder = pickle.load(file)

            
    def loadToken(self):
        with open('BModels/tokenizer.pickle', 'rb') as file:
            self.tokenizer = pickle.load(file)

    
    def preprocess_text(self , text):
        sequence = self.tokenizer.texts_to_sequences([text])
        sequence = keras.preprocessing.sequence.pad_sequences(sequence, truncating='post',maxlen=18)

        return sequence
    def load_dataset(self):
        with open('Datasets/intents.json', 'rb') as file:
            data = file.read()

        self.data = json.loads(data)

    def predict(self,text):
        self.loadEncoder()
        self.loadToken()
        self.load_dataset()
        p_text = self.preprocess_text(text)
        prediction = self.model.predict(p_text)
        predicted_label = np.argmax(prediction)
        tag = self.encoder.inverse_transform([predicted_label])[0]
        responce=""
        for i in self.data['intents']:
            if i['tag'] == tag:
                responce = np.random.choice(i['responses'])
        return responce



