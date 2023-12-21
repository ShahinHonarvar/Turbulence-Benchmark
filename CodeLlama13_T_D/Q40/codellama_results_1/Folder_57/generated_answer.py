
def return_n_smallest_chars(distinct_characters):
    sorted_list = sorted([*distinct_characters], key=ord)
    return sorted_list[:29]
