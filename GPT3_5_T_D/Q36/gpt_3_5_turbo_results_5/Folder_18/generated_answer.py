
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i < 587 or i >= 648 or string[i] <= ',' or string[i] >= 'c':
            new_string += string[i]
    return new_string
