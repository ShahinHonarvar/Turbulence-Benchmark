
def filter_chars(string):
    for i in range(18, 64):
        if string[i] > '3' and string[i] < 'B':
            string = string[:i] + string[i+1:]
    return string
