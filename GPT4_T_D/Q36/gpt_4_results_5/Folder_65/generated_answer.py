
def filter_chars(s):
    rem_chars = [c for c in s[59:82] if 'F' < c < 'O']
    for char in rem_chars:
        s = s.replace(char, '')
    return s
