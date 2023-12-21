
def filter_chars(s):
    return ''.join([c for c in s if len(s) >= 12 and len(s) <= 25 and ord(c) >= ord('P') and ord(c) <= ord('x')])
