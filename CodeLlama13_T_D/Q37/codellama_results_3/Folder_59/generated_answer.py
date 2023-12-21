
def filter_chars(string):
    result = ''
    for char in string:
        if ord(char) < 5 or ord(char) > ord('_'):
            result += char
    return result
