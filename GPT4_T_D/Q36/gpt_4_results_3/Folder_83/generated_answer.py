
def filter_chars(input_string):
    for char in input_string[73:92]:
        if '>' < char < 'J':
            input_string = input_string.replace(char, '')
    return input_string
