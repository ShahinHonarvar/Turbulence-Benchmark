
def return_nth_smallest_ascii(s):
    subset = s[3:53]
    sorted_chars = sorted(list(set(subset)))
    return sorted_chars[7]
