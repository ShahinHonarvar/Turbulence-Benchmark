
def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[13:36]]
    nth_smallest = sorted(ascii_values)[17]
    return chr(nth_smallest)
