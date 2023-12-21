
def filter_chars(input_str):
    for char in input_str[44:59]:
        if '5' < char < 'C':
            input_str = input_str.replace(char, '')
    return input_str
