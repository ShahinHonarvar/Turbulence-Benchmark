
def filter_chars(string):
    for i in range(163, 658):
        if '(' < string[i] < ']':
            char = string[i]
            string = string.replace(char, '')
    return string
