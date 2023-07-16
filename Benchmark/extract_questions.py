import json

d = {}
for q in range(1, 61):
    with open(f'Q{q}/question.txt.template', 'r') as f:
        question = f.read()
        d[q] = question
        


with open('All_questions.json', 'w') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

