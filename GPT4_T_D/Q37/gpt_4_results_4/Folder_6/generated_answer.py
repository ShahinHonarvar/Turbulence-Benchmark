
def filter_chars(s):
    substring = s[13:29]
    filtered_chars = [char for char in substring if char >= 'c' and char <= 'n']
    for char in set(filtered_chars):
        s = s.replace(char, '')
    return s
