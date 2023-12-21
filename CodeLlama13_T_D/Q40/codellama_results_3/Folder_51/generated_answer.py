
def return_n_smallest_chars(s):
    n = 45
    return sorted(set(s), key=lambda x: ord(x))[0:n]
