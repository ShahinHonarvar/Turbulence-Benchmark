
def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    return sorted(s[:7], reverse=True)
