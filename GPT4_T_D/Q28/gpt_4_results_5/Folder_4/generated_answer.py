
def return_nth_smallest_ascii(string):
    sub_string = string[9:23]
    ascii_vals = sorted([ord(ch) for ch in sub_string])
    return chr(ascii_vals[3])
