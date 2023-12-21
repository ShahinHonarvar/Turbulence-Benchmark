
def return_nth_smallest_ascii(string):
    substring = string[17:35]
    ascii_order = sorted(substring, key=ord)
    return ascii_order[17]
