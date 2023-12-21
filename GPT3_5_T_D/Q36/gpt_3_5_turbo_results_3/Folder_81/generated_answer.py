
def filter_chars(string):
    new_string = string[:51] + string[76:]
    for char in string[51:76]:
        if char > '5' and char < 'f':
            new_string = new_string.replace(char, '')
    return new_string
