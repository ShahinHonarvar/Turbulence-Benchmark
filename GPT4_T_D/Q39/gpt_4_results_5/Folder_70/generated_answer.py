
def return_n_greatest_chars(n):
    sorted_chars = sorted(n, key=ord, reverse=True)
    return sorted_chars[:2]
