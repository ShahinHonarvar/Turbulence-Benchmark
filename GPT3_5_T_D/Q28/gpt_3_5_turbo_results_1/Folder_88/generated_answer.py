
def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[38:65] if c in s]
    return sorted(filtered_chars)[13]
