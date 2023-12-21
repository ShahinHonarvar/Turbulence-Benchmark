
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    top_84_chars = sorted_chars[:84]
    top_84_chars.sort(reverse=True)
    return top_84_chars
