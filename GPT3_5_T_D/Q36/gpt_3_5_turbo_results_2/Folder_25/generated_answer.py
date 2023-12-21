
def filter_chars(string):
    new_string = string[:24] + string[37:]
    for char in string[24:37]:
        if 'A' < char < 'h':
            new_string = new_string.replace(char, '')
    return new_string
