
def return_n_smallest_chars(s):
    s = sorted(s, key=lambda x: ord(x))
    return sorted(s[:16], reverse=True)
