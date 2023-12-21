
def return_nth_smallest_ascii(s):
    s = list(s[0:5])
    s.sort(key=ord)
    return s[3]
