
def filter_chars(s):
    chars = [char for char in s[53:88] if '&' < char < 'c']
    for char in chars:
        s = s.replace(char, '')
    return s
