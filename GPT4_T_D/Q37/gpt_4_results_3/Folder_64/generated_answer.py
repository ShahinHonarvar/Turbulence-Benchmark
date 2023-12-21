
def filter_chars(str):
    indices_chars = set(str[1:8])
    filtered_chars = {c for c in indices_chars if 'L' <= c <= 'a'}
    return ''.join(c for c in str if c not in filtered_chars)
