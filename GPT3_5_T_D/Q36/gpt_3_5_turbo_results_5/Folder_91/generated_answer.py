
def filter_chars(string):
    for char in string[:3]:
        if '$' < char < '?':
            string = string.replace(char, '')
    return string
