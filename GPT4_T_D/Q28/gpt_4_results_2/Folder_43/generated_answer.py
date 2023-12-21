
def return_nth_smallest_ascii(s):
    substring = s[14:36]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[10]
