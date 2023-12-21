
def filter_chars(s):
    to_remove = {char for i, char in enumerate(s) if 38 <= i <= 99 and 'A' <= char <= 'Q'}
    return ''.join(char for char in s if char not in to_remove)
