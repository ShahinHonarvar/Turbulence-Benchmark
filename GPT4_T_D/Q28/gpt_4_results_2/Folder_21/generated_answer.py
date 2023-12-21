
def return_nth_smallest_ascii(str):
    sub_str = str[8:66]
    sorted_chars = sorted(sub_str, key=ord)
    return sorted_chars[5]
