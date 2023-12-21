
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 54 or i >= 92 or string[i] <= 'J' or string[i] >= 'X':
            filtered_string += string[i]
    return filtered_string
