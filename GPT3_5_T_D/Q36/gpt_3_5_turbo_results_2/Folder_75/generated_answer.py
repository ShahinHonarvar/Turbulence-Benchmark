
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 46 or i >= 74 or char <= '&' or char >= 'M':
            filtered_string += char
    return filtered_string
