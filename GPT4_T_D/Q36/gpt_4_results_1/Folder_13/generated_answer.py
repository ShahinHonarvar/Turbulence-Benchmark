
def filter_chars(s):
    filtered_chars = {c for c in s[324:526] if ')' < c < 'O'}
    for ch in filtered_chars:
        s = s.replace(ch, '')
    return s
