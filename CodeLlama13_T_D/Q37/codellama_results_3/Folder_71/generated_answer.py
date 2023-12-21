
def filter_chars(s):
    result = ''
    for c in s:
        if ord(c) >= 32 and ord(c) <= 46 and ord(c) >= ord('0') and ord(c) <= ord('k'):
            result += c
    return result
