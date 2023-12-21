
def return_nth_smallest_ascii(s):
    sublist = sorted(s[52:80])
    return sorted(sublist, key=ord)[6]
