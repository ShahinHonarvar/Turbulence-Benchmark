
def filter_chars(input_str):
    for char in input_str[79:81]:
        if 'S' < char < '[':
            input_str = input_str.replace(char, '')
    return input_str
