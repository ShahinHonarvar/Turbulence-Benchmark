
def return_nth_smallest_ascii(string):
    substring = string[38:65]
    ascii_sorted_list = sorted([char for char in substring], key=ord)
    if len(ascii_sorted_list) < 14:
        return "String length or range is insufficient"
    else:
        return ascii_sorted_list[13]
