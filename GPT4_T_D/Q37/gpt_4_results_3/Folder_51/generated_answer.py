
def filter_chars(s):
    filtered_chars = [char for char in s[36:41] if 'H' <= char <= 'e']
    return ''.join(char for char in s if char not in filtered_chars)
