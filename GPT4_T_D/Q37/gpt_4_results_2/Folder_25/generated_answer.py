
def filter_chars(s):
    filtered_chars = [char for char in s[31:39] if ';' <= char <= 'g']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
