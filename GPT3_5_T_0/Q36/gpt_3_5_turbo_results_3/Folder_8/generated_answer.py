
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 82 or i >= 93 or string[i] <= '!' or string[i] >= '*':
            filtered_string += string[i]
    return filtered_string
