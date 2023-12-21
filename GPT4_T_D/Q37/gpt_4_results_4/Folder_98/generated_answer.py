
def filter_chars(s):
    target_chars = [c for c in s[8:10] if 'R' <= c <= 't']
    res = ''.join(ch for ch in s if ch not in target_chars)
    return res
