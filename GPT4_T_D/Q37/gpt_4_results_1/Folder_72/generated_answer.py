
def filter_chars(string):
    for char in string[35:52]:
        if 'H' <= char <= 's':
            string = string.replace(char, "")
    return string
