
def return_nth_smallest_ascii(s):
    ascii_list = [ord(c) for c in s if 0 <= ord(c) <= 11]
    nth_smallest = sorted(ascii_list)[11]
    return chr(nth_smallest)
