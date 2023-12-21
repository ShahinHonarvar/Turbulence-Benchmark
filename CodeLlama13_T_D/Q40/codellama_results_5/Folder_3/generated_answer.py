
def return_n_smallest_chars(s):
    n = 28
    chars = []
    for c in s:
        if c not in chars and len(chars) < n:
            chars.append(c)
    return sorted(chars, reverse=True)
