import pickle
import numpy as np
import joblib
import spacy
import nltk
import spacy
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from tensorflow import keras
import re
class MyModel:

    def __init__(self):
        with open('Models/ChatModel.pickle', 'rb') as file:
            self.model = pickle.load(file)
        
    def loadEncoder(self):
        with open('Models/LabelEnoceder.pickle', 'rb') as file:
            self.encoder = pickle.load(file)

            
    def loadToken(self):
        with open('Models/tokenizer.pickle', 'rb') as file:
            self.tokenizer = pickle.load(file)

    
    def preprocess_text(self , text):
        print('from pre ' ,text)
        text = str(text)
        stem = " ".join([stemmer.stem(word) for word in re.sub(r'[^\w\s]','',text).split()])
#        stem= " ".join([stemmer.stem(word) for word in text.split()])
        sequence = self.tokenizer.texts_to_sequences([stem])
        sequence = keras.preprocessing.sequence.pad_sequences(sequence, maxlen=10)

        return sequence

    def predict(self,text):
        print('from model ',text)
        self.loadEncoder()
        self.loadToken()
        p_text = self.preprocess_text(text)
        print('from model p_text  ',p_text)
        prediction = self.model.predict(p_text)
        predicted_label = np.argmax(prediction)
        response = self.encoder.inverse_transform([predicted_label])[0]
        return response



