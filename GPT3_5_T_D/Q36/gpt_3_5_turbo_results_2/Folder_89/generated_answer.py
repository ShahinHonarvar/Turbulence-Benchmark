
def filter_chars(string):
    for char in string[57:69]:
        if '(' < char < 'W':
            string = string.replace(char, "")
    return string
