
def remove_repeat_chars(s):
    # Create a new string with the same characters as s, but without any repeated characters
    new_str = ""
    # Iterate through each character in s
    for char in s:
        # If the current character is not already in the new string
        if char not in new_str:
            # Add the current character to the new string
            new_str += char

    return new_str
