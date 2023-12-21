
def filter_chars(s):
    unique_chars = set(s[20:80])
    valid_chars = [char for char in unique_chars if '!' <= char <= 'T']
    for char in valid_chars:
        s = s.replace(char,'')
    return s
