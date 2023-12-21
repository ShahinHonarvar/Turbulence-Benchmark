
def return_nth_smallest_ascii(s):
    ascii_vals = []
    for c in s[48:76]:
        if c not in ascii_vals:
            ascii_vals.append(ord(c))
    ascii_vals.sort()
    return chr(ascii_vals[5])
