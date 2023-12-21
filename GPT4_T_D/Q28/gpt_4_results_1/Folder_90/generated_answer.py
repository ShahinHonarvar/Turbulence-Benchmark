
def return_nth_smallest_ascii(s):
    substr = s[17:84]
    ascii_values = [ord(ch) for ch in substr]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[4])
