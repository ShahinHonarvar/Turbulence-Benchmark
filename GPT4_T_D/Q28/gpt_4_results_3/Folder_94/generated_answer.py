
def return_nth_smallest_ascii(s):
    sliced_string = s[6:59]
    sorted_chars = sorted(sliced_string, key=ord)
    return sorted_chars[18]
