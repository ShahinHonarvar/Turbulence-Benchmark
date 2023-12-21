def filter_chars(s):
    return ''.join(c for c in s if c.isspace() or 521 <= ord(c) <= 722 and ord(c) >= '>')
