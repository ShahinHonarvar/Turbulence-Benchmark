
def filter_chars(s):
    filtered_chars = [c for c in s[75:100] if '8' <= c <= 'e']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
