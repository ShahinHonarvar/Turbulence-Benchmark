
def filter_chars(s):
    check_chars = [ch for ch in s[33:61] if '3' < ch < 'D']
    for c in check_chars:
        s = s.replace(c, "")
    return s
