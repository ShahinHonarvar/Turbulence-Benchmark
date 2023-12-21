
def filter_chars(string):
    new_string = string
    for char in string[1:9]:
        if '8' < char < 'm':
            new_string = new_string.replace(char, '')
    return new_string
