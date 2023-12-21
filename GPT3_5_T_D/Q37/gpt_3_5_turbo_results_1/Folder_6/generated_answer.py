
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 13 or i > 28 or string[i] < 'c' or string[i] > 'n':
            filtered_string += string[i]
    return filtered_string
