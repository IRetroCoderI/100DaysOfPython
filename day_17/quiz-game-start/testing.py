from data import question_data


print(question_data[0]['text'])

for question in question_data:
    print(question['text'])