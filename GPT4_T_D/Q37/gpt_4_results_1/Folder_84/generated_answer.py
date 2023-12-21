
def filter_chars(s):
    filtered_chars = {char for char in s[138:921] if '6' <= char <= 'A'}
    for char in filtered_chars:
        s = s.replace(char, '')

    return s
