
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i < 35 or i > 51 or string[i] < 'H' or string[i] > 's':
            new_string += string[i]
    return new_string
