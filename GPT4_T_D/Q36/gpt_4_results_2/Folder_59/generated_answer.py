
def filter_chars(string):
    for char in string[4:-2]:
        if '?' < char < 'k':
            string = string.replace(char, "")
    return string
