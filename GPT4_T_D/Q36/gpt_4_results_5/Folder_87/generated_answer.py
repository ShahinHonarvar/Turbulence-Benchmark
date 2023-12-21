
def filter_chars(s):
    target_chars = [ch for ch in s[33:61] if '3' < ch < 'D']
    for ch in target_chars:
        s = s.replace(ch, '')
    return s
