
def return_nth_smallest_ascii(string):
    char_set = set(string)
    ascii_vals = []
    for c in char_set:
        ascii_vals.append((ord(c), c))
    ascii_vals.sort()
    return ascii_vals[13][1]
