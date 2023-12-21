
def return_nth_smallest_ascii(string):
    ascii_vals = [ord(c) for c in string if 5 <= ord(c) <= 10]
    return chr(sorted(ascii_vals)[5])
