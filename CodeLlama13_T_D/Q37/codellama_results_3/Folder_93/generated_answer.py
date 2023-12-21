
def filter_chars(string):
    result = ''
    for char in string:
        if 38 <= ord(char) <= 69 and char >= 'H' and char <= 'e':
            continue
        result += char
    return result
