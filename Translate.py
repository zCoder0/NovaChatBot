from googletrans import Translator
from LangModel import LangsModel
class Translation:
    def __init__(self):
        self.translator = Translator()

    def detectLang(self ,text):
        l = LangsModel()
        lng = l.predict(text)
        return lng

    def translate (self, text , ln='en'):
        text = str(text)
        lng =self.detectLang(text)
    
        translated = self.translator.translate(text, src=str(lng), dest=ln)  # Translate from English to Spanish
        return str(translated.text) , lng
