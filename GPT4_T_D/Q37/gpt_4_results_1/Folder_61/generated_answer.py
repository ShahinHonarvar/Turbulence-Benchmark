
def filter_chars(my_string):
    to_remove = [c for c in my_string[5:7] if 'G' <= c <= 'p']
    return ''.join(c for c in my_string if c not in to_remove)
