
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if 22 <= string.index(char) <= 85 and '7' <= char <= 'e':
            continue
        filtered_string += char
    return filtered_string
