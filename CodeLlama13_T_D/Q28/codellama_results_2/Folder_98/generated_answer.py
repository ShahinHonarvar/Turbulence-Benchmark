
def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if ord(c) <= 8]
    return chr(sorted(ascii_values)[8])
