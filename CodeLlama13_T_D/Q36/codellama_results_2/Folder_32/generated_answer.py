
def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] > '7' and string[i] < 'H':
            continue
        else:
            new_string += string[i]
    return new_string
