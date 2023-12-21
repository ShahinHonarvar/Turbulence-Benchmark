
def return_nth_smallest_ascii(char_string):
    subset_string = char_string[0:70]
    sorted_chars = sorted(list(set(subset_string)))
    return sorted_chars[9]
