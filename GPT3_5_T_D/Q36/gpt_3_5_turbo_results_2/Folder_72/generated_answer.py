
def filter_chars(string):
    filtered_string = string[:44] + string[44:68].replace('x', '').replace('y', '').replace('z', '') + string[68:]
    return filtered_string
