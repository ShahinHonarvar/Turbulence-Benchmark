
def filter_chars(s):
    to_remove = [char for char in s[71:97] if '_' <= char <= 'o']
    return ''.join(char for char in s if char not in to_remove)
