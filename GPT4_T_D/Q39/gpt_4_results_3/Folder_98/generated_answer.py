
def return_n_greatest_chars(distinct_chars):
    sorted_chars = sorted(distinct_chars, key=ord, reverse=True)
    return sorted_chars[:68]
