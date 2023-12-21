
def filter_chars(string):
    result = ''
    for char in string:
        if ord(char) >= ord('I') and ord(char) <= ord('K'):
            result += char
    return result
