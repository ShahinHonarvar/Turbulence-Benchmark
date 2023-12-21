
def filter_chars(s):
    filtered_chars = [char for char in s[42:93] if '/' <= char <= 'a']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
