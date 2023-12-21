
def filter_chars(string):
    for i in range(1, len(string)):
        if '8'< string[i] < 'm':
            string = string.replace(string[i], '')
    return string
