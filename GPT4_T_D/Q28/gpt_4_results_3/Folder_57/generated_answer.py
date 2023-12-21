
def return_nth_smallest_ascii(s):
    sliced_str = s[17:35]
    sorted_chars = sorted(sliced_str, key=lambda x: ord(x))
    return sorted_chars[17]
