
def filter_chars(s):
    filtered_chars = [ch for ch in s[47:68] if ch > 'H' and ch < 's']
    return ''.join(ch for ch in s if ch not in filtered_chars)
