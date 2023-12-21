
def filter_chars(string):
    result = ""
    for i, c in enumerate(string[42:67]):
        if c > '6' and c < 'g':
            result += c
    return result + string[67:]
