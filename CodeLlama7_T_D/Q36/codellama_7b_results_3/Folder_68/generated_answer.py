
def filter_chars(string):
    for i in range(1, 9):
        if string[i] > '8' and string[i] < 'm':
            string = string[:i] + string[i+1:]
    return string
