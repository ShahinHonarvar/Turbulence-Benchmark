
def filter_chars(s):
    slice_chars = [char for char in s[83:93] if char > '!' and char < '*']
    for char in slice_chars:
        s = s.replace(char, '')
    return s
