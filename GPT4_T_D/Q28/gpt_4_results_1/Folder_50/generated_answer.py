
def return_nth_smallest_ascii(distinct_chars):
    sub_str = distinct_chars[25:89]
    sorted_chars = sorted(sub_str, key=ord)
    return sorted_chars[10]
