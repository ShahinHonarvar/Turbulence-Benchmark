
def filter_chars(string):
    result = ''
    for char in string:
        if ord(char) < 27 or ord(char) > 85 or ord(char) <= ord('!') or ord(char) >= ord('B'):
            result += char
    return result
