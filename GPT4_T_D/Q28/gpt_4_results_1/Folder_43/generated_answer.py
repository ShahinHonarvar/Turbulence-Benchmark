
def return_nth_smallest_ascii(str_input):
    subset_str = str_input[14:36]
    ascii_set = sorted([ord(ch) for ch in subset_str])
    if len(ascii_set) >= 11:
        return chr(ascii_set[10])
