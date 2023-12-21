
def return_n_greatest_chars(distinct_chars):
    sorted_chars = sorted(distinct_chars, key=ord, reverse=True)
    greatest_chars = sorted_chars[:10]
    return sorted(greatest_chars)
