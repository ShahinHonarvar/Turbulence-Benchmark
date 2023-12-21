
def filter_chars(string):
    result = ''
    for char in string:
        if ord(char) >= 227 and ord(char) <= 235 and char >= 'D' and char <= 'u':
            result += char
    return result
