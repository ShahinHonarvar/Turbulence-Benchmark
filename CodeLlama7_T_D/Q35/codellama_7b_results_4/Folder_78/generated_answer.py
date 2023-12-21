 def remove_repeat_chars(s):
    # Create a new string with the modified characters
    new_str = ""
    # Iterate over each character in the original string
    for char in s:
        # If the current character is not already in the new string
        if char not in new_str:
            # Add the current character to the new string
            new_str += char

    return new_str
