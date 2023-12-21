
def return_nth_smallest_ascii(char_string):
    relevant_chars = char_string[3:53]
    sorted_chars = sorted(relevant_chars, key=lambda x: ord(x))
    return sorted_chars[7]
