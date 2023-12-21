
def return_nth_smallest_ascii(char_string):
    char_substring = char_string[:12]
    sorted_chars = sorted(char_substring)
    return sorted_chars[11]
