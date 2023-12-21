
def return_nth_smallest_ascii(s):
    selected_chars = s[5:83]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[15]
