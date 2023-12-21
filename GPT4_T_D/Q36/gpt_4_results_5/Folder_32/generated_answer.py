
def filter_chars(inp_string):
    chars_to_remove = set([c for c in inp_string[41:63] if '7' < c < 'H'])
    return ''.join([c for c in inp_string if c not in chars_to_remove])
