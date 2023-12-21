
def filter_chars(string):
    for i in range(672, 709):
        if string[i] > 'X' and string[i] < '}':
            string = string.replace(string[i], '')
    return string
