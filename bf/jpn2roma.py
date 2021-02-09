import regex
import re
from pykakasi import kakasi

class JPN2Roman:
    def __init__(self):
        self.hiragana = regex.compile(r'\p{Script=Hiragana}+')
        self.katakana = regex.compile(r'\p{Script=Katakana}+')
        self.kanji = regex.compile(r'\p{Script=Han}+')
        self.kakasi = kakasi()
        self.kakasi.setMode('H','a')
        self.kakasi.setMode('K','a')
        self.kakasi.setMode('J','a')
        self.conv = self.kakasi.getConverter()

    def check(self, text:str)->bool:
        if self.hiragana.findall(text):
            return True
        if self.katakana.findall(text):
            return True
        if self.kanji.findall(text):
            return True
        return False
    
    def do(self, text:str)->str:
        return self.conv.do(text)
    

if __name__ == '__main__':
    instance = JPN2Roman()
    text = '乙乙'
    if instance.check(text):
        print(type(instance.do(text)),instance.do(text))
    text = 'Pikt'
    if instance.check(text):
        pass
    else:
        print(text)