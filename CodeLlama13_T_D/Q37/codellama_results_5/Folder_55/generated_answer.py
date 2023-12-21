
def filter_chars(s):
    chars = set()
    for i in range(1, 5+1):
        if s[i] >= "$" and s[i] <= ";":
            chars.add(s[i])
    return "".join([c for c in s if c not in chars])
