
def filter_chars(string):
    for i in range(26, 80):
        if string[i] == '>' or string[i] == '<':
            string = string[:i] + string[i+1:]
    return string
