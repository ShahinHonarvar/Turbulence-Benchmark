
def return_nth_smallest_ascii(s):
    if len(s) < 10:
        return "Input string is not long enough."
    s = s[:10]
    s = sorted(s, key=ord)
    return s[9]
