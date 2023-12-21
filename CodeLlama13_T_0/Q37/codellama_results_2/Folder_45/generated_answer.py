
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 72 or ord(char) > 94 or ord(char) < ord('.') or ord(char) > ord('b'):
            result += char
    return result
