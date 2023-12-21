
def filter_chars(s):
    indices_chars = set(s[i] for i in range(4, 8))
    filtered_chars = [c for c in indices_chars if c > '?' and c < 'k']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
