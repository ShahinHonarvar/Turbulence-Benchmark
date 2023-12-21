
def filter_chars(string):
    for char in string[22:25]:
        if '5' < char < '}':
            string = string.replace(char, '')
    return string
