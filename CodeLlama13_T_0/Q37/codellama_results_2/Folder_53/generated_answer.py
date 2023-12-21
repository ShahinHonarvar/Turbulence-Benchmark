
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 83 or ord(char) > 99 or ord(char) < ord('*') or ord(char) > ord('j'):
            result += char
    return result
