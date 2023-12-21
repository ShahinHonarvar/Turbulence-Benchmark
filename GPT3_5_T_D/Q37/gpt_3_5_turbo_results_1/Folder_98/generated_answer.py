
def filter_chars(string):
    filter_string = string[0:8] + string[9:]
    for char in string[8:10]:
        if char >= 'R' and char <= 't':
            filter_string = filter_string.replace(char, '')
    return filter_string
