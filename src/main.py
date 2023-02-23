import correct_answers_retriever

if __name__ == '__main__':
    model = 'Codex'  # Codex, Cohere
    number_of_tests = 3
    correct_answers, counter_examples = correct_answers_retriever.prepare_q_a(model, number_of_tests)
    num_passed = number_of_tests - len(counter_examples)
    num_failed = number_of_tests - num_passed
    counter = 1
    with open('test_verdict.txt', 'w') as f:
        print(f'Testing {model}\n')
        f.write(f'Testing {model}\n')
        print(f'Question {counter}\n')
        f.write(f'Question {counter}\n')
        print(
            f'Out of {number_of_tests} test cases, {number_of_tests - len(counter_examples)} passed and {len(counter_examples)} failed.')
        f.write(f'Out of {number_of_tests} test cases, {num_passed} passed and {num_failed} failed.\n')
        if counter_examples:
            for k, v in counter_examples.items():
                print('Counter examples:\n')
                f.write('Counter examples:\n')
                print(f'Prompt>>>\n{k}')
                f.write(f'Prompt>>>\n{k}\n')
                print(f'Generated code>>>\n{v[1]}')
                f.write(f'Generated code>>>\n{v[1]}\n')
                print(100 * '=', '\n')
                f.write(100 * '=')
                f.write('\n')

        if len(correct_answers) == 1:
            print('The only correct code was:')
            f.write(f'The only correct code was:')
            for i in correct_answers.values():
                print(i[1])
                f.write(f'{i[1]}\n')

        elif len(correct_answers) > 1:
            similar_layout_list = list(correct_answers_retriever.extract_common_layout(correct_answers))
            print(f'The common layout among the correct codes of {model} was:\n{similar_layout_list[0]}')
            f.write(f'The common layout among the correct codes of {model} was:\n{similar_layout_list[0]}')
