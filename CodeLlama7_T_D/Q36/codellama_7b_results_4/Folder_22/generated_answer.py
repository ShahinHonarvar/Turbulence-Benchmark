
def filter_chars(string):
    for i in range(55, 84):
        if string[i] > ';' and string[i] < 'z':
            string = string[:i] + string[i+1:]
    return string
