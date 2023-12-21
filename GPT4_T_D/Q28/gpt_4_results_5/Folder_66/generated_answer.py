
def return_nth_smallest_ascii(s):
    sub_str = s[35:53]
    sorted_chars = sorted(sub_str, key=ord)
    return sorted_chars[9]
