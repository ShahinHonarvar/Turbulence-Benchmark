
def return_nth_smallest_ascii(distinct_chars):
    subset_chars = distinct_chars[48:77]
    sorted_chars = sorted(subset_chars, key=lambda x: ord(x))
    return sorted_chars[4]
