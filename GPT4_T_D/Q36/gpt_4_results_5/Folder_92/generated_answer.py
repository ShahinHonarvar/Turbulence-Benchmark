
def filter_chars(input_str):
    for char in input_str[2:6]:
        if ','< char < 'f':
            input_str = input_str.replace(char,'')
    return input_str
