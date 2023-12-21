
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 24 or i >= 37 or string[i] <= 'A' or string[i] >= 'h':
            filtered_string += string[i]
    return filtered_string
