
def return_n_smallest_chars(distinct_chars):
    return sorted([char for char in distinct_chars], key=ord)[:23]
