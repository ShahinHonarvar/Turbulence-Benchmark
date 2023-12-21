
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string
    indices = [i for i, c in enumerate(string) if c != ""]
    # Check if the indices are valid
    if not (28 <= min(indices) and max(indices) <= 54):
        return None

    # Get the characters at the specified indices
    chars = [string[i] for i in indices]
    # Sort the characters by their ASCII value
    sorted_chars = sorted(chars, key=ord)
    # Return the character with the 14th smallest ASCII value
    return sorted_chars[13]
