
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if 51 <= ord(char) <= 96 and 'X' <= char <= 'p':
            continue
        filtered_string += char
    return filtered_string
