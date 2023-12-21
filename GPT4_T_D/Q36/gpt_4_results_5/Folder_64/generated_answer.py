
def filter_chars(string):
    for char in string[2:7]:
        if '3' < char < '^':
            string = string.replace(char, '')
    return string
