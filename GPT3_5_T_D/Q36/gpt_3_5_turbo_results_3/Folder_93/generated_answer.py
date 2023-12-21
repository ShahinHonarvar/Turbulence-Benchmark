
def filter_chars(string):
    filtered_str = ""
    for i in range(len(string)):
        if i < 52 or i >= 88 or string[i] <= '&' or string[i] >= 'c':
            filtered_str += string[i]
    return filtered_str
