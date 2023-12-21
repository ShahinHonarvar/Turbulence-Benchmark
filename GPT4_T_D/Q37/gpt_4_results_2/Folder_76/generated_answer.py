
def filter_chars(s):
    subset_chars = set(filter(lambda x: 'M' <= x <= 'v', s[379:899]))
    for char in subset_chars:
        s = s.replace(char, "")
    return s
