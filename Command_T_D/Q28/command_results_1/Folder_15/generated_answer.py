
def return_nth_smallest_ascii(s):
    return s[s.index(min(s, key=lambda x: ord(x) // 3)) + 1:s.index(min(s, key=lambda x: ord(x) // 3)) + 6]
