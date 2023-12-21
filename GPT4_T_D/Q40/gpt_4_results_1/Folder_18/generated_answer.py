
def return_n_smallest_chars(distinct_chars):
    sorted_chars = sorted(distinct_chars, key=ord)
    top_52_chars = sorted_chars[:52]
    top_52_chars.sort(reverse=True)
    return top_52_chars
