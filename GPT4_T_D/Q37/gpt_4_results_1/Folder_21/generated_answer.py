
def filter_chars(s):
    filtered_chars = [c for c in s[603:760] if 'Q' <= c <= 'h']
    for c in filtered_chars:
        s = s.replace(c, '')
    return s
