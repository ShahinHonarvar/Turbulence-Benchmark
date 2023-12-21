
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)[:37]
    return sorted_chars[::-1]
