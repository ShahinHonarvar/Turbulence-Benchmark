
def return_nth_smallest_ascii(s):
    substring = s[25:65]
    return sorted(substring, key=ord)[5]
