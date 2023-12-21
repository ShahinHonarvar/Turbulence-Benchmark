
def return_nth_smallest_ascii(s):
    sublist = list(s[17:87])
    sublist.sort(key=ord)
    return sublist[14]
