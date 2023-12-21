
def return_nth_smallest_ascii(s):
    sublist = list(s[28:68])
    ascii_values = [ord(ch) for ch in sublist]
    sorted_ascii = sorted(ascii_values)
    if len(sorted_ascii) >= 15:
        return chr(sorted_ascii[14])
    else:
        return None
