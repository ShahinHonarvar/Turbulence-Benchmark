
def return_nth_smallest_ascii(string):
    chars = string[17:87]
    distinct_chars = set(chars)
    sorted_chars = sorted(distinct_chars)
    return sorted_chars[14]
