
def return_nth_smallest_ascii(s):
    s = s[:88]
    sorted_s = sorted(s, key=ord)
    return sorted_s[13]
