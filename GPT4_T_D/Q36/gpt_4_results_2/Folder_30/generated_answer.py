
def filter_chars(s):
    filtered_chars = [c for c in s[24:45] if c > '3' and c < 'I']
    for c in filtered_chars:
        s = s.replace(c, '')
    return s
