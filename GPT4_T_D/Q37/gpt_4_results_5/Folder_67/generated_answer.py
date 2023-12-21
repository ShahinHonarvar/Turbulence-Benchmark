
def filter_chars(str_to_filter):
    chars_to_remove = set()
    for i, c in enumerate(str_to_filter):
        if 19 <= i <= 22 and ']' <= c <= 't':
            chars_to_remove.add(c)
    return ''.join([c for c in str_to_filter if c not in chars_to_remove])
