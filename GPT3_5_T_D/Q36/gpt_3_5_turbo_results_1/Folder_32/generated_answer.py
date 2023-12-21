
def filter_chars(string):
    new_string = string[:40] + string[63:]
    for char in string[40:63]:
        if '7' < char < 'H':
            new_string = new_string.replace(char, '')
    return new_string
