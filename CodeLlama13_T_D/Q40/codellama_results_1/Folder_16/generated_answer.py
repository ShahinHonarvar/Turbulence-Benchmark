
def return_n_smallest_chars(distinct_chars):
    sorted_chars = sorted([char for char in distinct_chars], key=ord)[:64]
    return sorted_chars[::-1]
