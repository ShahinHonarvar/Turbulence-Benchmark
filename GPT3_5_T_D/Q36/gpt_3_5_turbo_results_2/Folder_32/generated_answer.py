
def filter_chars(string):
    for i in range(40, 63):
        if string[i] > '7' and string[i] < 'H':
            string = string.replace(string[i], "")
    return string
