
def return_nth_smallest_ascii(s):
    return min([c for c in s[21:59+1] if ord(c) <= 122], key=ord)
