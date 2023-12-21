
def filter_chars(string):
    for char in string[14:40]:
        if ':' < char < 'C':
            string = string.replace(char, "")
    return string
