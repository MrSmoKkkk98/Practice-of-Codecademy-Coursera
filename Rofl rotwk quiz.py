from question import Question

question_prompts = [
    'How many stats buff add to units in rotwk 2.02?\n(a) + 33% and + 25 % armor and damage\n(b) + 33 % and + 33 % armor and damage\n(c) + 50 % and + 50 % armor and damage\n\n',
    'How many Glorfindel cost?\n(a) 1700\n(b) 1705\n(c) 1600\n\n',
    'Who is the best player in rotwk 2.02?\n(a) Smaug\n(b) Smusch\n(c) Smug\n\n'
]

questions = [
    Question(question_prompts[0], 'b'),
    Question(question_prompts[1], 'b'),
    Question(question_prompts[2], 'c'),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f'You got {score} / {len(questions)} Correct')


run_test(questions)
