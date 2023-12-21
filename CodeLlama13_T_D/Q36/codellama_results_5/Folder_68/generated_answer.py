
def filter_chars(string):
    filtered = ""
    for i, char in enumerate(string):
        if 1 < ord(char) < 9 and ord(char) > 8 and ord(char) < ord('m'):
            filtered += char
    return filtered
