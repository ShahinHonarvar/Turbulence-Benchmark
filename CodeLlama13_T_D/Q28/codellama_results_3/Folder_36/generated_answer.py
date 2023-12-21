
def return_nth_smallest_ascii(s):
    s = s[17:56]
    ascii_values = []
    for c in set(s):
        ascii_values.append((c, ord(c)))
    ascii_values.sort(key=lambda x: x[1])
    return ascii_values[8][0]
