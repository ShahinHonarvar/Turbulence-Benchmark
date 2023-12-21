
def return_nth_smallest_ascii(s):
    n = 17
    indices = range(12, 56)
    chars = [c for c in s if ord(c) in indices]
    return sorted(chars)[n-1]
