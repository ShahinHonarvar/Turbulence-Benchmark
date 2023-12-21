
def filter_chars(string):
    filtered = ""
    for char in string:
        if ord(char) < 155 or ord(char) > 403 or (ord(char) >= ord('(') and ord(char) <= ord(']')):
            filtered += char
    return filtered
