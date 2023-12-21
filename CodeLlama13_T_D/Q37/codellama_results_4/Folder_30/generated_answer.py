
def filter_chars(s):
    result = ""
    for i, c in enumerate(s):
        if 41 <= i <= 64 and ord('K') <= ord(c) <= ord(']'):
            continue
        result += c
    return result
