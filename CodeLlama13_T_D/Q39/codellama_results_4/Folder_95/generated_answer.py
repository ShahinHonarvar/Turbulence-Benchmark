
def return_n_greatest_chars(s):
    chars = []
    for c in s:
        if c not in chars:
            chars.append(c)
    chars.sort(key=ord)
    return chars[:36]
