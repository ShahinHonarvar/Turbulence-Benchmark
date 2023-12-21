
def return_n_greatest_chars(s):
    if len(s) != len(set(s)):
        raise ValueError('The string should contain distinct characters only.')
    s_sorted = sorted(s, key=ord, reverse=True)
    return s_sorted[0:35]
