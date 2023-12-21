
def return_nth_smallest_ascii(s):
    subset_chars = list(s[17:84])
    subset_chars.sort(key=ord)
    return subset_chars[4]
