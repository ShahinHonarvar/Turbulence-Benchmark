
def filter_chars(input_str):
    for char in input_str[12:46]:
        if '!' < char < 'A':
            input_str = input_str.replace(char, '')
    return input_str
