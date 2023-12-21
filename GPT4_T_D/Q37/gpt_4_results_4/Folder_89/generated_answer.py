
def filter_chars(s):
    selective_chars = set([char for char in s[11:33] if '!' <= char <= '@'])
    new_string = ''.join([char for char in s if char not in selective_chars])
    return new_string
