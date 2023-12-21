
def filter_chars(input_string):
    targeted_chars = []
    for index in range(78, 87):
        if index < len(input_string) and ';' < input_string[index] < 'r':
            targeted_chars.append(input_string[index])
    for char in set(targeted_chars):
        input_string = input_string.replace(char, '')
    return input_string
