
def filter_chars(str_val):
    to_remove = set(ch for ch in str_val[503:754] if '9' <= ch <= 'w')
    return ''.join(ch for ch in str_val if ch not in to_remove)
