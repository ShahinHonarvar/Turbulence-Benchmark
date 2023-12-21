
def filter_chars(s):
    removed_chars = [char for char in s[51:78] if 'V' <= char <= 'Y']
    return ''.join(char for char in s if char not in removed_chars)
