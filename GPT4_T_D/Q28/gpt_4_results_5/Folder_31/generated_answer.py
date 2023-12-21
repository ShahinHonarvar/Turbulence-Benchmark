
def return_nth_smallest_ascii(text):
    chars_between_indices = text[10:83]
    sorted_chars = sorted(chars_between_indices)
    return sorted_chars[17]
