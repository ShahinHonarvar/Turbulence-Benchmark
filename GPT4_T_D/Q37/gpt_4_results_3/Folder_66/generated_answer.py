
def filter_chars(s):
    to_remove = set([ch for ch in s[27:86] if 'c' <= ch <= 'i'])
    filtered_string = ''.join([ch for ch in s if ch not in to_remove])
    return filtered_string
