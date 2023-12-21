
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 2 or i >= 7 or string[i] <= 'h' or string[i] >= 'k':
            filtered_string += string[i]
    return filtered_string
