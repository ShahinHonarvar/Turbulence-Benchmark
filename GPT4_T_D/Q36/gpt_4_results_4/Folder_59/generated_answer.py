
def filter_chars(s):
    filtered = [ch for ch in s[4:8] if '?' < ch < 'k']
    for char in filtered:
        s = s.replace(char, '')
    return s
