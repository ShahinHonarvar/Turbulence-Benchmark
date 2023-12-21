
def filter_chars(str):
    chars_to_remove = set([c for c in str[2:4] if '5' <= c <= '_'])
    new_str = "".join([c for c in str if c not in chars_to_remove])
    return new_str
