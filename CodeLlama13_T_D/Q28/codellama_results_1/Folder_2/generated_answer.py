
def return_nth_smallest_ascii(string):
    ascii_vals = []
    for i in range(48, 76+1):
        if string[i] not in ascii_vals:
            ascii_vals.append(ord(string[i]))
    return chr(sorted(ascii_vals)[4])
