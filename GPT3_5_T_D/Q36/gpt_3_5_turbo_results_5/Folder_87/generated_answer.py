
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i < 32 or i > 61 or string[i] <= '3' or string[i] >= 'D':
            new_string += string[i]
    return new_string
