
def filter_chars(string):
    for character in string[300:418]:
        if '9' < character < 'P':
            string = string.replace(character, '')
    return string
