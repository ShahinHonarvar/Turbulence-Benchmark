
def filter_chars(s):
    result = ""
    for i, c in enumerate(s):
        if i < 19 or i > 32 or ord(c) < ord('f') or ord(c) > ord('o'):
            result += c
    return result
