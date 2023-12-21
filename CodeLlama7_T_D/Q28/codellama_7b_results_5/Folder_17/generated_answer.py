
def return_nth_smallest_ascii(s):
    # Convert the string to a list of characters
    chars = list(s)
    # Sort the list of characters by their ASCII values
    sorted_chars = sorted(chars, key=ord)
    # Return the 4th smallest ASCII value among the characters in the sorted list
    return sorted_chars[3]
