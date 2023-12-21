
def filter_chars(string):
    for char in string[1:6]:
        if char >= '$' and char <= ';':
            string = string.replace(char, '')
    return string
