
def filter_chars(string):
    for i in range(91, 97):
        char = chr(i)
        if ord('j') < ord(char) < ord('w'):
            string = string.replace(char, '')
    return string
