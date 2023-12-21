
def return_nth_smallest_ascii(string):
    substring = string[13:36]  # Extract substring between indices 13 to 35
    sorted_chars = sorted(substring)  # Sort the characters in ascending order
    return sorted_chars[17]  # Return the character at index 17 (18th smallest ASCII value)
