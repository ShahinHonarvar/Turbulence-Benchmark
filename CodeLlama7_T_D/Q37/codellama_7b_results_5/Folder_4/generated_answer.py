
def filter_chars(string):
    for i in range(19, 34):
        if string[i] >= 'S' and string[i] <= '{':
            string = string.replace(string[i], '', 1)
    return string
