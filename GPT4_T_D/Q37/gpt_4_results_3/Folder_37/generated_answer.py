
def filter_chars(s):
    substring = set(s[17:64])
    filtered_chars = {char for char in substring if 'O' <= char <= '^'}
    result = [char for char in s if char not in filtered_chars]
    return ''.join(result)
