
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 35 or i >= 60 or string[i] <= '!' or string[i] >= 'B':
            filtered_string += string[i]
    return filtered_string
