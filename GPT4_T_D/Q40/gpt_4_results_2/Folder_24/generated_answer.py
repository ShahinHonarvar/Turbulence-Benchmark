
def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    return s[:32][::-1]
