
def return_nth_smallest_ascii(character_string):
    relevant_chars = character_string[24:72]
    sorted_chars = sorted(relevant_chars, key=ord)
    return sorted_chars[7]
