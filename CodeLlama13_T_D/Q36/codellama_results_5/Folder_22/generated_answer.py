
def filter_chars(string):
    filtered = ''
    for i in range(55, 84):
        if string[i].isalpha() and ';' < string[i] < 'z':
            filtered += string[i]
    return filtered
