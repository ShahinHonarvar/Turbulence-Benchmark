
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if 33 <= ord(c) <= 70 and ord(c) >= ord('7') and ord(c) <= ord('k'):
            result += c
    return result
