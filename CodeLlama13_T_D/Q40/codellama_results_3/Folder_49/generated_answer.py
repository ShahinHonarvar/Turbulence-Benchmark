
def return_n_smallest_chars(s):
    chars = list(set(s))
    sorted_chars = sorted(chars, key=ord)[:76]
    return sorted_chars
