
def return_n_smallest_chars(distinct_string):
    sorted_list = sorted(distinct_string, key=ord)[:10]
    return sorted_list
