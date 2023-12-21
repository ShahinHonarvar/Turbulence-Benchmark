
def filter_chars(s):
    chars_to_remove = set()
    for i in range(20, min(80, len(s))):
        if '!' <= s[i] <= 'T':
            chars_to_remove.add(s[i])
    new_str = ''
    for c in s:
        if c not in chars_to_remove:
            new_str += c
    return new_str
