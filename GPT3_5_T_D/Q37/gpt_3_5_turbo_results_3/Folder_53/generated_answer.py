
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 83 or i > 99 or string[i] < '*' or string[i] > 'j':
            filtered_string += string[i]
    return filtered_string
