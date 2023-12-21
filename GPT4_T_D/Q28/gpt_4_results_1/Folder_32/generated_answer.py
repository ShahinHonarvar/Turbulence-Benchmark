
def return_nth_smallest_ascii(s):
    ascii_chars = [char for i, char in enumerate(s) if 14<=i<=66]
    sorted_chars = sorted(ascii_chars, key=ord)
    return sorted_chars[7]
