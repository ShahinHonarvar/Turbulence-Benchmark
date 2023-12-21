
def filter_chars(my_str):
    remove_chars = set([c for i, c in enumerate(my_str) if 114 <= i <= 639 and '!' <= c <= 'x'])
    return ''.join([c for c in my_str if c not in remove_chars])
