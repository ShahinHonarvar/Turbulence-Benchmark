
def return_nth_smallest_ascii(s):
    sub_string = s[67:78]
    sorted_sub_string = sorted(sub_string, key=ord)
    return sorted_sub_string[6]
