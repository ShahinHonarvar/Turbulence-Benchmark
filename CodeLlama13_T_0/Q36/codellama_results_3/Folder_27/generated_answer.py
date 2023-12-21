
def filter_chars(string):
    new_str = ""
    for i in range(48, 75):
        if string[i] > '6' and string[i] < '_':
            new_str += string[:i] + string[i+1:]
        else:
            new_str += string[i]
    return new_str
