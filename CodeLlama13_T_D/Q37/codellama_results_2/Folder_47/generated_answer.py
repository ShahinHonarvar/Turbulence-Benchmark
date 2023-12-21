
def filter_chars(s):
    result = ""
    for i, c in enumerate(s):
        if i >= 38 and i <= 54 and ord(c) >= ord(':') and ord(c) <= ord('r'):
            result += c
        else:
            result += c
    return result
