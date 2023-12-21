
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 73 or ord(char) > 74 or ord(char) < ord('U') or ord(char) > ord('l'):
            result += char
    return result
