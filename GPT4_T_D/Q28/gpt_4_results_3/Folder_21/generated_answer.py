
def return_nth_smallest_ascii(s):
    sublist = list(s[8:66])
    sublist.sort(key=ord)
    return sublist[5]
