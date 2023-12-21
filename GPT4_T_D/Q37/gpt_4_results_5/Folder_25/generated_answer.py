
def filter_chars(s):
    filter_chars = set([ch for ch in s[31:39] if ';' <= ch <= 'g'])
    return ''.join([ch for ch in s if ch not in filter_chars])
