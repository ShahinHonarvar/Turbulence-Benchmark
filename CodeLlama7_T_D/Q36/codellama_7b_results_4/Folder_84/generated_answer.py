
def filter_chars(string):
    for i in range(171, 636):
        if string[i] > 'c' and string[i] < 's':
            string = string[:i] + string[i+1:]
    return string
