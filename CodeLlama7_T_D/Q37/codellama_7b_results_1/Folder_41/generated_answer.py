
def filter_chars(string):
    for i in range(26, 64 + 1):
        if string[i] >= 'V' and string[i] <= 'o':
            string = string[:i] + string[i + 1:]
    return string
