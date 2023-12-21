
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if 31 <= i < 70 and ord(c) > ord('B') and ord(c) < ord('v'))
