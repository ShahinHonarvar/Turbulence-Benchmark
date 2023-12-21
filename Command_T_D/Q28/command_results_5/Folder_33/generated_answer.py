
def return_nth_smallest_ascii(s):
    ascii_s = [c for c in s if 0x20 <= ord(c) <= 0x7E]
    return sorted(ascii_s)[22]
