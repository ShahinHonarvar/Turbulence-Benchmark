
def return_nth_smallest_ascii(s):
    sublist = list(s[10:83])
    sublist.sort(key=ord)
    return sublist[17]
