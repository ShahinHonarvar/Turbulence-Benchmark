
def return_nth_smallest_ascii(s):
    substring = s[14:67]
    sorted_chars = sorted([char for char in substring], key=ord)
    return sorted_chars[7]
