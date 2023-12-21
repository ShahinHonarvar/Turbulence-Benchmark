
def filter_chars(s):
    return ''.join([c for c in s if ord(c) < 722 or ord(c) > 832 or (ord('K') <= ord(c) <= ord('m'))])
