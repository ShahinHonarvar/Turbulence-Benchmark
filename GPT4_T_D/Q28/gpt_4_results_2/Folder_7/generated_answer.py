
def return_nth_smallest_ascii(s):
    substring = s[12:56]
    sorted_substring = sorted(substring, key=ord)
    return sorted_substring[16]
