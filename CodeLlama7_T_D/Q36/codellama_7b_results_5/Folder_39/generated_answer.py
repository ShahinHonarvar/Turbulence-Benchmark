
def filter_chars(string):
    for i in range(43, 59):
        if string[i] > '5' and string[i] < 'C':
            string = string[:i] + string[i+1:]
    return string
