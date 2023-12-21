
def return_nth_smallest_ascii(s):
    s = s[:88]
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[13]
