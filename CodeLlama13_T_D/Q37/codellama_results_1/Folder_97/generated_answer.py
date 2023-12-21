
def filter_chars(string):
    filtered = ''
    for char in string:
        if ord(char) < 227 or ord(char) > 235 or ord(char) < 68 or ord(char) > 117:
            filtered += char
    return filtered
