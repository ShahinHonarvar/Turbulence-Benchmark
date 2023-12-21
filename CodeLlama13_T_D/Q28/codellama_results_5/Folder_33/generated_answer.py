
def return_nth_smallest_ascii(string):
    ascii_vals = []
    for char in string[22:75]:
        if char not in ascii_vals:
            ascii_vals.append(ord(char))
    ascii_vals.sort()
    return chr(ascii_vals[11])
