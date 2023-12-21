
def filter_chars(input_string):
    for char in input_string[220:403]:
        if '*' < char < '7':
            input_string = input_string.replace(char, '')
    return input_string
