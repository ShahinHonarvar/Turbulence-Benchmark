
def return_nth_smallest_ascii(s):
    s = s[3:53]
    sorted_s = sorted(s, key=ord)
    return sorted_s[7]
