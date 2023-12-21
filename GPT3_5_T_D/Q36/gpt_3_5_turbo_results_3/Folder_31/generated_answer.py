
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 14 or i >= 75 or string[i] <= '9' or string[i] >= 'K':
            filtered_string += string[i]
    return filtered_string
