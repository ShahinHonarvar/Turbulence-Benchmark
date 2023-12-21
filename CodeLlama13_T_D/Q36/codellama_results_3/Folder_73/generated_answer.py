
def filter_chars(string):
    result = ''
    for char in string:
        if ord(char) > ord('#') and ord(char) < ord('T'):
            result += char
        else:
            result += ''.join([c for c in string if c != char])
    return result
