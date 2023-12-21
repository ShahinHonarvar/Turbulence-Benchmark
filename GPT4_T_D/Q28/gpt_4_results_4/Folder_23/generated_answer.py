
def return_nth_smallest_ascii(string):
    charlist = list(string[29:48])
    charlist.sort(key=ord)
    return charlist[6]
