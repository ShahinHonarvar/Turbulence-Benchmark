
def return_nth_smallest_ascii(char_string):
    subset_chars = char_string[51:61]
    if len(subset_chars) < 5:
        return 'Not enough characters!'
    sorted_chars = sorted(subset_chars, key=ord)
    return sorted_chars[4]
