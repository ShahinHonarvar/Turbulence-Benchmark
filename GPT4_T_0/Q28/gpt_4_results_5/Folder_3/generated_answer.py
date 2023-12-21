
def return_nth_smallest_ascii(s):
    s = s[25:46]
    sorted_s = sorted(s, key=ord)
    return sorted_s[10]
