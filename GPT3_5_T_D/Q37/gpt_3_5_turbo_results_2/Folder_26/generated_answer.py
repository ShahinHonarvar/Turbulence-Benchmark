
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if 20 <= string.index(char) <= 62 and 'i' <= char <= 'k':
            continue
        filtered_string += char
    return filtered_string
