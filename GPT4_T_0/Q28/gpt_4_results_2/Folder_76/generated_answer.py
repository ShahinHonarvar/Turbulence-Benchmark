
def return_nth_smallest_ascii(s):
    s = s[18:67]
    sorted_s = sorted(s, key=ord)
    return sorted_s[18]
