
def return_nth_smallest_ascii(s):
    ascii_sorted = sorted(s[:19], key=ord)
    return ascii_sorted[18]
