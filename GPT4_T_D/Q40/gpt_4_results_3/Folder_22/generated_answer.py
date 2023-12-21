
def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=ord)[:76]
    return sorted_s
