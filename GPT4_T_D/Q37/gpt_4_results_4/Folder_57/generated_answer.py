
def filter_chars(string):
    for i in range(27, min(86,len(string))):
        if '!' <= string[i] <= 'B':
            string = string.replace(string[i], "")
    return string
