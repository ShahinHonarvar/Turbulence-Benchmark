
def filter_chars(s):
    char_set = set(s[42:93]) & set(chr(i) for i in range(ord('/'), ord('a')+1))
    res = "".join([c for c in s if c not in char_set])
    return res
