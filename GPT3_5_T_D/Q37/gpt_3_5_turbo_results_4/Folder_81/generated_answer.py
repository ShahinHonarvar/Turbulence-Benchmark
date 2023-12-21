
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i < 19 or i > 92 or string[i] < '8' or string[i] > 'm':
            new_string += string[i]
    return new_string
