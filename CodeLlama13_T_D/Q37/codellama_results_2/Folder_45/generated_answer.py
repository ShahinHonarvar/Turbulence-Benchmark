
def filter_chars(string):
    new_str = ""
    for i in range(72, 95):
        if string[i].isalpha() and string[i] >= '.' and string[i] <= 'b':
            new_str += string[i]
    return new_str
