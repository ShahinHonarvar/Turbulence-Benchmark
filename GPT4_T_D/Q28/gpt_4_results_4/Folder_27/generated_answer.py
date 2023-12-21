
def return_nth_smallest_ascii(s):
    sub_str = s[33:86]
    sorted_sub_str = sorted(sub_str, key=lambda x: ord(x))
    return sorted_sub_str[12]
