
def filter_chars(string):
    result = ""
    for char in string:
        if ord(char) < 227 or ord(char) > 235 or (ord(char) >= ord('D') and ord(char) <= ord('u')):
            result += char
    return result
