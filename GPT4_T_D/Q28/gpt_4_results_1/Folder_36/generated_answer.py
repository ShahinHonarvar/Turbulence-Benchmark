
def return_nth_smallest_ascii(string):
    relevant_chars = string[17:57]
    sorted_chars = sorted(relevant_chars, key=lambda char: ord(char))
    return sorted_chars[8]
