
def filter_chars(s):
    flagged_chars = [char for char in s[521:723] if '>' <= char <= '_']
    return ''.join(char for char in s if char not in flagged_chars)
