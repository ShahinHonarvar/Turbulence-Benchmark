
def return_n_smallest_chars(s):
    s = sorted(s)
    s = s[:7]
    s.sort(reverse=True)
    return s
