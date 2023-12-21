
def return_n_greatest_chars(distinct_chars):
    greatest_chars = sorted(distinct_chars, key=ord, reverse=True)[:36]
    return sorted(greatest_chars)
