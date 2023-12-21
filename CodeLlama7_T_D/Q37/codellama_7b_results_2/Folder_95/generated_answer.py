
def filter_chars(string):
    for i in range(35, 41):
        if string[i] >= ')' and string[i] <= 'l':
            string = string[:i] + string[i+1:]
    return string
