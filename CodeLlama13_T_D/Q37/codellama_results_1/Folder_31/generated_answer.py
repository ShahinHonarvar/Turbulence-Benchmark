
def filter_chars(string):
    filtered = ""
    for char in string:
        if ord(char) < 57 or ord(char) > 96 or (ord(char) >= ord('<') and ord(char) <= ord('w')):
            filtered += char
    return filtered
