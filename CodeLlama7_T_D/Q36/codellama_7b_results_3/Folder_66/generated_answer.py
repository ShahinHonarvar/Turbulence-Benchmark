
def filter_chars(string):
    for i in range(39, 87):
        if string[i] > '!' and string[i] < '}':
            string = string[:i] + string[i+1:]
    return string
