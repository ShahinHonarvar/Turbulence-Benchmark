
def return_nth_smallest_ascii(s):
    s = list(set(s[6:59]))
    s.sort(key=ord)
    return s[18]
