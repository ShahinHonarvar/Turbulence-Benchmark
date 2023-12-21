
def filter_chars(string):
    filtered = ''
    for i in range(25, 98):
        if string[i] >= 'm' and string[i] <= 'w':
            filtered += string[i]
    return filtered
