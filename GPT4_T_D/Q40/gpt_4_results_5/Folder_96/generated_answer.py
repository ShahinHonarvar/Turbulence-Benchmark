
def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    top_20_chars = sorted_chars[:20]
    top_20_chars = sorted(top_20_chars, reverse=True)
    return top_20_chars
