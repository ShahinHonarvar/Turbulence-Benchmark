
def filter_chars(s):
    chars = {c: None for c in s[324:526] if c > ')' and c < 'O'}
    return ''.join([c for c in s if c not in chars])
