
def filter_chars(s):
    return ''.join([c for c in s if not (90 >= ord(c) >= 19 and ord(c) <= ord('h') and ord(c) >= ord('F'))])
