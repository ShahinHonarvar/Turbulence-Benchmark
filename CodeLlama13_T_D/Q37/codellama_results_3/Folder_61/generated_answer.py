
def filter_chars(string):
    result = ''
    for char in string:
        if ord(char) < 71 and ord(char) > 69:
            continue
        else:
            result += char
    return result
