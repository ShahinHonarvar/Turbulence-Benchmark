
def filter_chars(string):
    for i in range(86, 93):
        if (string[i] >= '!' and string[i] <= 's'):
            string = string[:i] + string[i+1:]
    return string
