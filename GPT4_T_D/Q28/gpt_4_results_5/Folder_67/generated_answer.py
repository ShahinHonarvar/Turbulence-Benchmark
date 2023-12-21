
def return_nth_smallest_ascii(s):
    substring = s[60:84]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[13]
