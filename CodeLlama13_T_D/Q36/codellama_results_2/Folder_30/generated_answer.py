
def filter_chars(string):
    for i in range(23, 45):
        if string[i].isalpha() and ord(string[i]) > ord('3') and ord(string[i]) < ord('I'):
            string = string.replace(string[i], '')
    return string
