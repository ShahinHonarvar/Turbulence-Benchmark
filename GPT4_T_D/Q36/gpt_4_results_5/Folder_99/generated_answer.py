
def filter_chars(string):
    for char in string[477:948]:
        if 'b' < char < 'd':
            string = string.replace(char, "")
    return string
