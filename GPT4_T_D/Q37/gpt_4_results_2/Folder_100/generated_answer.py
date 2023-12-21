
def filter_chars(s):
    filtered_chars = [char for char in s[88:91] if not (char >= 'J' and char <= 'Q')]
    for char in set(s[88:91]) - set(filtered_chars):
        s = s.replace(char, '')
    return s
