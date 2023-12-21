
def return_nth_smallest_ascii(s):
    return s[s.rfind("a", 20, 80) + 1:s.rfind("z", 20, 80) + 1]
