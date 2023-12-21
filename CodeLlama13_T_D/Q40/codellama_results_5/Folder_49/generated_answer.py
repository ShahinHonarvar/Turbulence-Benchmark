
def return_n_smallest_chars(s):
    chars = {}
    for c in s:
        if c not in chars:
            chars[c] = ord(c)
    sorted_chars = sorted(chars, key=lambda x: chars[x])[:76]
    return "".join(sorted_chars)
