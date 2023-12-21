
def return_n_smallest_chars(s):
    if len(s) < 9:
        return []
    return sorted(s, key=ord)[:9][::-1]
