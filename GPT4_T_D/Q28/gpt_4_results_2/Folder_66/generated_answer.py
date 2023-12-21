
def return_nth_smallest_ascii(s):
    substring = s[35:53]
    ascii_sorted_chars = sorted(substring, key=lambda x: ord(x))
    return ascii_sorted_chars[9]
