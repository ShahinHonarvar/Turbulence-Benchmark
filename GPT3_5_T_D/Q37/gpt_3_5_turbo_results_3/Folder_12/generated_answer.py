
def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i < 19 or i > 90 or string[i] < 'F' or string[i] > 'h':
            new_string += string[i]
    return new_string
