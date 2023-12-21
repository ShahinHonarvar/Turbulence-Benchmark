
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] < 'J' or string[i] > 'X':
            new_string += string[i]
    return new_string
