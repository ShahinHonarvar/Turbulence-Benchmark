
def filter_chars(string):
    result = ''
    for char in string:
        if char >= 'H' and char <= 's':
            result += char
    return result
