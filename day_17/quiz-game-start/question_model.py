# 'Create a Question class with an __init()__ method with two attribtes: text and answer attribute'
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
q1 = Question('The Earth is flat.', 'False')
print(q1.answer)