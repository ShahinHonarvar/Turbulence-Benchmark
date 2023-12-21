
def return_nth_smallest_ascii(s):
    ascii_values = {ord(c) for c in s[17:56]}
    nth_smallest_ascii = sorted(ascii_values)[8]
    return chr(nth_smallest_ascii)
