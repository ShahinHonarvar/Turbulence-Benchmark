
def filter_chars(string):
    result = ''
    for char in string:
        if ord(char) > 53 and ord(char) < 67:
            continue
        result += char
    return result
