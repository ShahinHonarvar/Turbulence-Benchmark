
def return_nth_smallest_ascii(s):
    s = s[12:73]
    sorted_str = sorted(s, key=ord)
    return sorted_str[12]
