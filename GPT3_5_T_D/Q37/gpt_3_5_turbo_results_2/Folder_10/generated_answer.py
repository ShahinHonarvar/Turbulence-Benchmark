
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 63 <= i <= 84 and 'E' <= char <= '~':
            filtered_string += string.replace(char, '')
        else:
            filtered_string += char
    return filtered_string
