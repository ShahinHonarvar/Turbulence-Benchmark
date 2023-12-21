
def filter_chars(string):
    new_str = ""
    for i in range(15, 85):
        if string[i].isalpha() and string[i] > 'I' and string[i] < 'M':
            new_str += string[i]
    return new_str
