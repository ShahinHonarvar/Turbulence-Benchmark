
def filter_chars(string):
    filtered = ''
    for char in string:
        if ord(char) > ord('F') and ord(char) < ord('n') and 45 < ord(char) < 57:
            continue
        filtered += char
    return filtered
