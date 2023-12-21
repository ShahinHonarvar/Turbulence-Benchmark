
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if i < 61 or i > 70 or ord(c) < ord('0') or ord(c) > ord('@'):
            result += c
    return result
