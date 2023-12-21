
def return_n_smallest_chars(s):
    s = sorted(s, key=ord)[:37]
    return sorted(s, reverse=True)
