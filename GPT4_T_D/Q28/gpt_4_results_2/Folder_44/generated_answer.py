
def return_nth_smallest_ascii(s):
    selected_chars = s[20:31]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[7] if len(sorted_chars) > 7 else None
