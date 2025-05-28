# question is presented to the user, and the user responds with either True or False
from question_model import Question
from data import question_data

question_bank = [] # holds Question objects
for question in question_data:
    q = Question(question['text'], question['answer'])
    question_bank.append(q)
        
#print(question_bank[0].text) for accessing each object's attributes