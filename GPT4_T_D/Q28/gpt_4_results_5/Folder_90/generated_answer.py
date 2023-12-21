
def return_nth_smallest_ascii(s):
    extracted_chars = list(s[17:84])
    ascii_sorted_chars = sorted(extracted_chars, key=ord)
    return ascii_sorted_chars[4]
