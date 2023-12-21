
def return_n_smallest_chars(s):
    s = sorted(s, key=lambda x: ord(x))
    if len(s) > 82:
        s = s[:82]
    return sorted(s, reverse=True)
