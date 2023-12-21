
def filter_chars(string):
    new_string = string[:587] + string[648:]
    for char in string[587:648]:
        if ',' < char < 'c':
            new_string = new_string.replace(char, '')
    return new_string
