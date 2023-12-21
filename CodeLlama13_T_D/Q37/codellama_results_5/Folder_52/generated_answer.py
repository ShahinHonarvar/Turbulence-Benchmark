
def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i >= 54 and i <= 83 and string[i] >= 'j' and string[i] <= 'v':
            continue
        new_string += string[i]
    return new_string
