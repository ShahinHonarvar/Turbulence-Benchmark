
def filter_chars(s):
    filtered = [char for char in s[12:26] if char >= 'P' and char <= 'x']
    for char in filtered:
        s = s.replace(char, '')
    return s
