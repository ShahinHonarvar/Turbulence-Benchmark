
def filter_chars(s):
    chars = [char for char in s[12:78] if char >= ':' and char <= 'L']
    return ''.join(char for char in s if char not in chars)
