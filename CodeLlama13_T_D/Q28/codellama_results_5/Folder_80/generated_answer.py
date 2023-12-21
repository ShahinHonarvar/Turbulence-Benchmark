
def return_nth_smallest_ascii(s):
    ascii_values = []
    for c in s[51:89]:
        if c not in ascii_values:
            ascii_values.append(ord(c))
    ascii_values.sort()
    return chr(ascii_values[13])
