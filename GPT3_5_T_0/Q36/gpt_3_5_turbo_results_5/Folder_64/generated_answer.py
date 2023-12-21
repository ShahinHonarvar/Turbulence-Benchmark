
def filter_chars(string):
    for char in string[1:7]:
        if '3' < char < '^':
            string = string.replace(char, '')
    return string
