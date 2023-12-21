
def return_nth_smallest_ascii(s):
    # Get the indices of all characters in the string
    indices = [i for i, c in enumerate(s) if s.count(c) > 1]
    # Filter out the indices that are not between 25 and 88 (inclusive)
    filtered_indices = []
    for i in indices:
        if 25 <= i <= 88:
            filtered_indices.append(i)
    # Get the characters at the filtered indices
    chars = [s[i] for i in filtered_indices]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(chars, key=ord)
    # Return the 11th smallest ASCII value
    return sorted_chars[10]
