
def filter_chars(string):
    filtered = ""
    for char in string:
        if not (ord(';') <= ord(char) <= ord('g')) or ord(char) < 31 or ord(char) > 38:
            filtered += char
    return filtered
