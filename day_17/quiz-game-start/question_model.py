# 'Create a Question class with an __init__() method with two attribtes: text and answer attribute'
from data import question_data

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

