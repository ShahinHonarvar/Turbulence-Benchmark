
def return_nth_smallest_ascii(s):
    selected_chars = s[:17]
    sorted_chars = sorted(selected_chars, key=lambda x: ord(x))
    return sorted_chars[16]
