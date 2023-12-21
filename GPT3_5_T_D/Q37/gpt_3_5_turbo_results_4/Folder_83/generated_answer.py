
def filter_chars(string):
    for i in range(29, len(string)):
        if string[i] >= 'K' and string[i] <= 'z':
            string = string.replace(string[i], "")
    return string
