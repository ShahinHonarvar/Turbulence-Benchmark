
def return_nth_smallest_ascii(s):
    indexed_s = s[:88]
    sorted_chars = sorted(list(set(indexed_s)))
    return sorted_chars[13]
