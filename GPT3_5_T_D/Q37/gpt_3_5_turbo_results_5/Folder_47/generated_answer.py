
def filter_chars(string):
    for i in range(38, 55):
        char = chr(i)
        if ':' <= char <= 'r' and char in string:
            string = string.replace(char, '')
    return string
