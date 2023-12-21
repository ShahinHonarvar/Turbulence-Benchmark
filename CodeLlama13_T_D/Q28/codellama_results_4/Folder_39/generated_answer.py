
def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[1:67]]
    nth_smallest = sorted(ascii_values)[8]
    return chr(nth_smallest)
