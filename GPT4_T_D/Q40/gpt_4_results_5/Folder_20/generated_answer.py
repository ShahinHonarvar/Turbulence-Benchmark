
def return_n_smallest_chars(s):
    s_sorted = sorted(s, key=lambda x: ord(x))
    return s_sorted[:40]
