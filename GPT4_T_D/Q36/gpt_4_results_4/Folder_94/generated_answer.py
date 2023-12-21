
def filter_chars(input_str):
    for character in input_str[16:85]:
        if 'I' < character < 'M':
            input_str = input_str.replace(character, "")
    return input_str
