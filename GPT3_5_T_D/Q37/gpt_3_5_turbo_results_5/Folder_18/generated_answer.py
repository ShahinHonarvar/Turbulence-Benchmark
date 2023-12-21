
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (770 <= i <= 970 and '-' <= c <= 'D'))
