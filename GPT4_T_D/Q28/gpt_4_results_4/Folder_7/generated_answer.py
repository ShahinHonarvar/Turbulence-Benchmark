
def return_nth_smallest_ascii(s):
    sublist = s[12:56]
    sorted_sublist = sorted(sublist, key=ord)
    return sorted_sublist[16]
