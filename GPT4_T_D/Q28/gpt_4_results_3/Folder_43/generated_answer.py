
def return_nth_smallest_ascii(s):
    s_modified = s[14:36]
    sorted_s = sorted(s_modified, key=ord)
    return sorted_s[10]
