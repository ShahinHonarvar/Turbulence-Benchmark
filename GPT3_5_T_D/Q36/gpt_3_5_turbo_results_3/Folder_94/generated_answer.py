
def filter_chars(string):
    new_string = string[:15] + string[85:]
    for char in string[15:85]:
        if 'I' < char < 'M':
            new_string = new_string.replace(char, "")
    return new_string
