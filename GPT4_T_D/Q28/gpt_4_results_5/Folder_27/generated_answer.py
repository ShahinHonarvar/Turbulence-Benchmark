
def return_nth_smallest_ascii(s):
    sub_string = s[33:86]
    sorted_chars = sorted(sub_string, key=ord)
    return sorted_chars[12]
