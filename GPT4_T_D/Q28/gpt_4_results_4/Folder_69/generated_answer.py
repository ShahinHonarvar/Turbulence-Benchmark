
def return_nth_smallest_ascii(s):
    selected_chars = s[67:78]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[6]
