
def return_nth_smallest_ascii(s):
    s = s[47:81]
    s = sorted(s, key=ord)
    return s[3]
