
def filter_chars(s):
    altered = [c for c in s[7:9] if 'B' <= c <= 'H']
    return ''.join(ch for ch in s if ch not in altered)
