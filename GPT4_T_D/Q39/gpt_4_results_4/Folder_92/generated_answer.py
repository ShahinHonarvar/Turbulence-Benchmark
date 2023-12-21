
def return_n_greatest_chars(st):
    sorted_chars = sorted(st, reverse=True)[:63]
    return sorted(sorted_chars)
