
def filter_chars(string):
    for i in range(24, 37):
        if string[i] > 'A' and string[i] < 'h':
            string = string[:i] + string[i+1:]
    return string
