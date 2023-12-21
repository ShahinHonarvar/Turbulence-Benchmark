
def filter_chars(s):
    changed_chars = {char for idx, char in enumerate(s) if 52 <= idx <= 81 and 'A' <= char <= 'U'}
    return ''.join(char for char in s if char not in changed_chars)
