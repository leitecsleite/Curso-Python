questions = [
    {
        'Question': 'Quanto é 2 + 2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'Quanto é 5 * 5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'Quanto é 10 / 2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    }
]

correct_count = 0
incorrect_count = 0

for question in questions:
    print('Question:', question['Question'])
    print()

    options = question['Options']

    for i, option in enumerate(options):
        print(f'{i})', option)
    print()

    choice = input('Escolha uma opção: ')

    correct = False
    choice_int = None

    num_options = len(options)

    if choice.isdigit():
        choice_int = int(choice)

    if choice_int is not None:
        if 0 <= choice_int < num_options:
            if options[choice_int] == question['Answer']:
                correct = True

    if correct:
        print('Correto')
        correct_count += 1
    else:
        print('Irrado')
        incorrect_count += 1

    print()

    print('Você acertou', correct_count, 'de', len(questions), 'questões.')