
def return_nth_smallest_ascii(s):
    sublist = list(s[25:78])
    sorted_sublist = sorted(sublist, key=ord)
    return sorted_sublist[15]
