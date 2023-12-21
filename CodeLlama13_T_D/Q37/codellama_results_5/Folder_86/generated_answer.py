
def filter_chars(string):
    result = ''
    for char in string:
        if char >= 'O' and char <= '}':
            result += char
    return result
