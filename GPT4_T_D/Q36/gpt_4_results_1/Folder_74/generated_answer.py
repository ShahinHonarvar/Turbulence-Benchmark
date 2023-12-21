
def filter_chars(string):
    for char in string[34:36]:
        if '>' < char < 'A':
            string = string.replace(char, "")
    return string
