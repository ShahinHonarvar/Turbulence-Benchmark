
def return_n_smallest_chars(chars):
    sorted_chars = sorted([char for char in chars], key=ord)
    n_smallest_chars = sorted_chars[:61]
    return sorted(n_smallest_chars, reverse=True)
