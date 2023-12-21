
def filter_chars(s):
    char_range = set(s[26:65])
    filtered_chars = [ch for ch in char_range if 'V' <= ch <= 'o']
    for ch in filtered_chars:
        s = s.replace(ch, '')
    return s
