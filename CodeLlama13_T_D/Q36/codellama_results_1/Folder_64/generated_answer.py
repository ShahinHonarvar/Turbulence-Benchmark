
def filter_chars(string):
    new_str = ''
    for i in range(1, 7):
        if string[i] > '3' and string[i] < '^':
            continue
        else:
            new_str += string[i]
    return new_str
