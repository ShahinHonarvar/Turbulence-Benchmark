
def filter_chars(s):
    filtered_chars = s[373:902]
    for char in filtered_chars:
        if 'T' <= char <= 'h':
            s = s.replace(char, "")
    return s
