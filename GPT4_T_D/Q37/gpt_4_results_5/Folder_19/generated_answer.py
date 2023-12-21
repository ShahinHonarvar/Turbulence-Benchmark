
def filter_chars(source_str):
    indices_str = source_str[35:90]
    chars_to_remove = [c for c in indices_str if 'E'<=c<='t']
    return ''.join([c for c in source_str if c not in chars_to_remove])
