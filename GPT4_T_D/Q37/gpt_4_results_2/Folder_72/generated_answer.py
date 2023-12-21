
def filter_chars(s):
    chars = list(s[35:52])
    filtered = [ch for ch in chars if ch < 'H' or ch > 's']
    for ch in filtered:
        s = s.replace(ch, '')
    return s
