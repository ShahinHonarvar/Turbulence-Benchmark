
def filter_chars(string):
    return string[:669] + ''.join(c for c in string[669:888] if c <= 'B' or c >= 'Y') + string[888:]
