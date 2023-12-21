
def return_nth_smallest_ascii(s):
    sliced_str = s[50:77]
    sorted_str = sorted(sliced_str, key=ord)
    return sorted_str[10]
