
def return_nth_smallest_ascii(s):
    sub_string = s[10:91]
    sorted_string = sorted(sub_string, key=ord)
    return sorted_string[19]
