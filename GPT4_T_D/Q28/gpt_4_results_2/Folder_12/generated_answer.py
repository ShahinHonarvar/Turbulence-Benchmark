
def return_nth_smallest_ascii(s):
    sub_s = s[3:27]
    ordered_chars = sorted(sub_s)
    return ordered_chars[4]
