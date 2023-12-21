
def filter_chars(string):
    for i in range(63, 89):
        if ord(string[i]) > ord('*') and ord(string[i]) < ord('w'):
            string = string.replace(string[i], '')
    return string
