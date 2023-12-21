
def return_nth_smallest_ascii(s):
    sublist = list(s[12:88])
    sublist.sort(key=ord)
    return sublist[16]
