
def filter_chars(string):
    dist_chars = [char for char in string[11:73] if 'i' <= char <= 'v']
    return ''.join(char for char in string if char not in dist_chars)
