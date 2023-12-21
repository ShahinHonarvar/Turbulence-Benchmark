
def return_nth_smallest_ascii(s):
    substring = s[5:48]
    sorted_chars = sorted(list(substring))
    return sorted_chars[12]
