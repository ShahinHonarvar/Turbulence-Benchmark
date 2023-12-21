
def filter_chars(s):

    filtered_chars = [ch for ch in set(s[503:946]) if ch > 'W' and ch < 'y']
    
    for char in filtered_chars:
        s = s.replace(char, '')

    return s
