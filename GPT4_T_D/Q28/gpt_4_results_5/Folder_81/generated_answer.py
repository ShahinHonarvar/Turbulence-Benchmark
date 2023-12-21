
def return_nth_smallest_ascii(s):
    char_list = sorted([char for char in s[:14]], key=ord)
    return char_list[13]
