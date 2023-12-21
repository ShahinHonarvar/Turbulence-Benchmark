
def return_nth_smallest_ascii(s):
    if len(s) > 69:
        tenth_char = sorted(s[:70])[9]
    else:
        tenth_char = sorted(s)[9]
    return tenth_char
