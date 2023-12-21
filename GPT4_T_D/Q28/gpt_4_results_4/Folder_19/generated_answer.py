
def return_nth_smallest_ascii(s):
    if len(s) > 18:
        s = s[:19]
    sorted_s = sorted(s, key=ord)
    return sorted_s[12]
