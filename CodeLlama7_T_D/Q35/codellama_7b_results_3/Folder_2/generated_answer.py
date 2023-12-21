
def remove_repeat_chars(s):
    # Create a new string that will contain the altered characters
    new_str = ""
    # Iterate over each character in the given string
    for char in s:
        # If the current character is not already present in the new string
        if char not in new_str:
            # Add the current character to the new string
            new_str += char

    # Return the altered string
    return new_str
