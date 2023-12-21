
def filter_chars(string):
    for i in range(3, 5):
        char = string[i]
        if ord('Y') < ord(char) < ord('s'):
            string = string.replace(char, '')
    return string
