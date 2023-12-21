
def filter_chars(my_string):
    selected_chars = set([c for i, c in enumerate(my_string) if 259 <= i <= 502 and ',' <= c <= '3'])
    return ''.join([c for c in my_string if c not in selected_chars])
