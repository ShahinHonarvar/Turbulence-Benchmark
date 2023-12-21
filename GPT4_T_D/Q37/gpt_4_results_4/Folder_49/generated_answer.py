
def filter_chars(s):
    filter_chars = [char for char in s[42:98] if '*' <= char <= 'b']
    filtered_str = ''.join(char for char in s if char not in filter_chars)
    return filtered_str
