
def filter_chars(s):
    res = ''
    for c in s:
        if ord(c) < 88 or ord(c) > 90 or ord(c) < ord('J') or ord(c) > ord('Q'):
            res += c
    return res
