
def return_nth_smallest_ascii(char_str):
    if len(char_str) > 69:
        char_str = char_str[0:70]
    sorted_chars = sorted(char_str, key=ord)
    return sorted_chars[9]
