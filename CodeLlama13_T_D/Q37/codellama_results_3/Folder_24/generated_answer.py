
def filter_chars(string):
    for i in range(36, 80):
        if string[i].isalpha() and ord(string[i]) >= ord('2') and ord(string[i]) <= ord('s'):
            string = string.replace(string[i], '')
    return string
