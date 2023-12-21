
def filter_chars(s):
    filtered_chars = [ch for ch in s[64:89] if '*' < ch < 'w']
    for ch in set(filtered_chars):
        s = s.replace(ch, "")
    return s
