
def return_nth_smallest_ascii(s):
    ascii_s = [c for c in s if c.isalpha()]
    ascii_s.sort()
    return ascii_s[len(ascii_s) - 16]
