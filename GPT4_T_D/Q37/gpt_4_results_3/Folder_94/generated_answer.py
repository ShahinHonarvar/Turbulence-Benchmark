
def filter_chars(s):
    forbidden_chars = {char for i, char in enumerate(s) if 51 <= i <= 96 and 'X' <= char <= 'p'}
    return ''.join(char for char in s if char not in forbidden_chars)
