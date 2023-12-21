
def filter_chars(string):
    new_str = ''
    for i in range(len(string)):
        if string[i] > 'f' and string[i] < '~':
            new_str += string[i]
    return new_str
