from googletrans import Translator
import language_tool_python 
from LangModel import LangsModel
class Translation:
    def __init__(self):
        self.translator = Translator()

    def detectLang(self ,text):
        l = LangsModel()
        lng = l.predict(text)
        return lng
    
    def correct_grammar(self,text):
        # Initialize the LanguageTool model for English
        tool = language_tool_python.LanguageTool('en-US')
        
        # Correct grammar and spelling mistakes
        matches = tool.check(text)
        corrected_text = language_tool_python.utils.correct(text, matches)
        return corrected_text

    def translate (self, text , ln='en'):
        text = str(text)
        lng =self.detectLang(text)
        if lng == "English":
            text = self.correct_grammar(text)
        translated = self.translator.translate(text, src=str(lng), dest=ln)  # Translate from English to Spanish
        return str(translated.text) , lng

