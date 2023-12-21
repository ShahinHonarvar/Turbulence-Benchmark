
def filter_chars(string):
    new_string = string[0]
    for char in string[1:7]:
        if '-' < char < 'L':
            new_string += string.replace(char, '')
    new_string += string[7:]
    return new_string
