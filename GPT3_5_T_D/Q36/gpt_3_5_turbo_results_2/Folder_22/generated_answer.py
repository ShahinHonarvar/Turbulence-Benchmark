
def filter_chars(string):
    for char in string[55:84]:
        if ';' < char < 'z':
            string = string.replace(char, "")
    return string
