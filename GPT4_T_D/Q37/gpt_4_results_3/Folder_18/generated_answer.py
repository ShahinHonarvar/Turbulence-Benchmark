
def filter_chars(s):
    index_range = s[770:971]
    special_chars = [c for c in index_range if '-' <= c <= 'D']
    for char in special_chars:
        s = s.replace(char, '')
    return s
