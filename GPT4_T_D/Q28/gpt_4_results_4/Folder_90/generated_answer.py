
def return_nth_smallest_ascii(s):
    relevant_chars = s[17:84]
    ascii_sorted = sorted(relevant_chars, key=ord)
    return ascii_sorted[4]
