
def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=ord)
    return sorted_s[:9][::-1]
