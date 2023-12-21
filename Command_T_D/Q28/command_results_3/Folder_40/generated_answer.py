
def return_nth_smallest_ascii(s):
    return s[s.index(min(s[0:4])) + 1]
