
def filter_chars(s):
    chars_to_filter = set([c for c in s[15:75] if '9' < c < 'K'])
    filtered_s = ''.join([c for c in s if c not in chars_to_filter])
    return filtered_s
