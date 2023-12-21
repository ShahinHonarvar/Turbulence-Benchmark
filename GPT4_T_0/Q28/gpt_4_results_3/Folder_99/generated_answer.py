
def return_nth_smallest_ascii(s):
    s = s[17:66]
    sorted_s = sorted(s, key=ord)
    return sorted_s[7]
