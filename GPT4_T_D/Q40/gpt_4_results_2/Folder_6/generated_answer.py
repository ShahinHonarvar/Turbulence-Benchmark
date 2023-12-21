
def return_n_smallest_chars(s):
    s = sorted(s)
    s = s[:47]
    s.sort(reverse=True)
    return s
