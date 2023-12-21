
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    n_greatest_chars = sorted_chars[:5]
    return sorted(n_greatest_chars)
