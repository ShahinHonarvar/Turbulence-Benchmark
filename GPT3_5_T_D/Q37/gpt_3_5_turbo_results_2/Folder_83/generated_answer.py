
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 29 or i > 79 or string[i] < 'K' or string[i] > 'z':
            filtered_string += string[i]
    return filtered_string
