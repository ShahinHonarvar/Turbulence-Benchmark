
def filter_chars(s):
    removal_chars = {char for i, char in enumerate(s) if 225 <= i <= 381 and 'D' <= char <= 'Y'}
    return ''.join(char for char in s if char not in removal_chars)
