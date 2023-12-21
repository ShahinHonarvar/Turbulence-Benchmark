
def return_nth_smallest_ascii(s):
    if len(s) > 17:
        s = s[0:17]
    sorted_s = sorted(s)
    return sorted_s[16]
