
def filter_chars(string):
    filtered = ""
    for char in string:
        if 52 <= ord(char) <= 81 and 'A' <= char <= 'U':
            continue
        filtered += char
    return filtered
