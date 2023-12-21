
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    fifty_nine_smallest_chars = sorted_chars[:59]
    fifty_nine_smallest_chars_sorted_desc = fifty_nine_smallest_chars[::-1]
    return fifty_nine_smallest_chars_sorted_desc
