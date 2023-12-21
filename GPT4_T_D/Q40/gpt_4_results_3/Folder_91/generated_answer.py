
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    six_smallest_chars = sorted_chars[:6]
    six_smallest_chars.sort(reverse=True)
    return six_smallest_chars
