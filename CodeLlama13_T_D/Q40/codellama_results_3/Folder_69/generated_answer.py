
def return_n_smallest_chars(s):
    sorted_chars = sorted(list(set(s)), key=ord)[:65]
    return sorted_chars[::-1]
