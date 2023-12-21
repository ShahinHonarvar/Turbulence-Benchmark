
def return_nth_smallest_ascii(s):
    # Get the indices of all characters in the string
    indices = [i for i, c in enumerate(s) if c != ""]
    # Filter out the indices that are not between 25 and 64 (inclusive)
    filtered_indices = [i for i in indices if 25 <= i <= 64]
    # Get a list of all characters at the filtered indices
    chars = [s[i] for i in filtered_indices]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(chars, key=ord)
    # Return the 6th smallest character
    return sorted_chars[5]
