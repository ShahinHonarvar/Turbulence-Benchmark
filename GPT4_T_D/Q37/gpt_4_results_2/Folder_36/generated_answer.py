
def filter_chars(s):
    filtered_chars = [c for c in s[259:503] if c >= ',' and c <= '3']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
