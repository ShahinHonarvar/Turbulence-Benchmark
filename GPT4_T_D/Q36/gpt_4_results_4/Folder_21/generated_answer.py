
def filter_chars(string):
    for char in string[220:403]:
        if '*' < char < '7':
            string = string.replace(char, '')
    return string
