
def return_nth_smallest_ascii(distinct_chars):
    distinct_chars = distinct_chars[5:83]
    sorted_chars = sorted(distinct_chars, key=ord)
    return sorted_chars[15]
