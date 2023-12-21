
def filter_chars(input_str):
    for char in input_str[28:75]:
        if 'A' < char < 'i':
            input_str = input_str.replace(char, '')
    return input_str
