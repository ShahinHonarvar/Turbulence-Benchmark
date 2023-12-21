
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 283 or i >= 484 or string[i] <= 'l' or string[i] >= 't':
            filtered_string += string[i]
    return filtered_string
