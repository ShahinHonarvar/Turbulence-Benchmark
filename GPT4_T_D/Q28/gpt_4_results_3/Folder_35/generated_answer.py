
def return_nth_smallest_ascii(s):
    sublist = sorted(s[50:76])
    return sorted(sublist, key=ord)[6]
