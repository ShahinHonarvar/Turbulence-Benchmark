
def filter_chars(string):
    for i in range(21, 26):
        if string[i] > '5' and string[i] < '}':
            string = string[:i] + string[i+1:]
    return string
