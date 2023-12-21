
def filter_chars(s):
    filtered_chars = [c for c in s[56:66] if c > 'f' and c < '|']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
