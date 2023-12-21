
def filter_chars(s):
    return s[:669] + ''.join(c for c in s[669:888] if c <= 'B' or c >= 'Y') + s[888:]
