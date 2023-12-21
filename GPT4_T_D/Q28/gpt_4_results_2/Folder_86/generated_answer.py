
def return_nth_smallest_ascii(s):
    s_substring = s[44:70]
    sorted_chars = sorted(s_substring, key=ord)
    return sorted_chars[14]
