
def return_nth_smallest_ascii(s):
    return sorted([ord(c) for c in s if 3 <= ord(c) <= 52])[7]
