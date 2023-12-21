
def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] >= '6' and string[i] < 'g':
            continue
        else:
            new_string += string[i]
    return new_string
