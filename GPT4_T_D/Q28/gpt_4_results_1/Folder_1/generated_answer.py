
def return_nth_smallest_ascii(string):
    sub_str = string[21:60]
    sorted_chars = sorted(sub_str, key=ord)
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    return None
