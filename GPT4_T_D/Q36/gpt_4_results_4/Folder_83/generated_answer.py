
def filter_chars(s):
    filtered_chars = [c for c in s[73:93] if c > '<' and c < 'J']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
