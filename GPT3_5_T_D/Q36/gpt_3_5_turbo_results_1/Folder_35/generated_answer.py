
def filter_chars(string):
    for i in range(163, 658):
        if '(' < string[i] < ']':
            string = string.replace(string[i], '')
    return string
