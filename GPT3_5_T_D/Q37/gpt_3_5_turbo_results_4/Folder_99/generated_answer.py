
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 373 or i > 901 or string[i] < 'T' or string[i] > 'h':
            filtered_string += string[i]
    return filtered_string
