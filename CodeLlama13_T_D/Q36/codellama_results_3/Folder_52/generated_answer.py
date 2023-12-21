
def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if (i >= 49 and i < 56) and string[i] > 'I' and string[i] < 'a':
            continue
        else:
            new_string += string[i]
    return new_string
