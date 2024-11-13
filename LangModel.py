import pickle
class LangsModel:

    def __init__(self):
        with open('LangModels/Language_Detection_Model2.pkl', 'rb') as file:
            self.model = pickle.load(file)
        
    def loadEncoder(self):
        with open('LangModels/lang_label_encoder.pkl', 'rb') as file:
            self.encoder = pickle.load(file)

            
    def loadToken(self):
        with open('LangModels/lang_count_vectorizer.pkl', 'rb') as file:
            self.cv= pickle.load(file)


    def predict(self,text):
        self.loadEncoder()
        self.loadToken()
        x = self.cv.transform([text]).toarray()
        lang = self.model.predict(x)
        lang = self.encoder.inverse_transform(lang)[0]
        return lang



