
def filter_chars(input_str):
    for char in input_str[44:83]:
        if ':' < char < 'Q':
            input_str = input_str.replace(char, '')
    return input_str
