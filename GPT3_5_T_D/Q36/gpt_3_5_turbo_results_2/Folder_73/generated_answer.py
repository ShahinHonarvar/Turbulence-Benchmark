
def filter_chars(s):
    return ''.join(c for c in s if ord(c) <= ord('#') or ord(c) >= ord('T') or ord(c) < 66 or ord(c) >= 90)
