
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 23 or i >= 45 or string[i] <= '3' or string[i] >= 'I':
            filtered_string += string[i]
    return filtered_string
