 def remove_repeat_chars(s):
    # Create a new empty string
    new_string = ""
    # Iterate through each character in the given string
    for char in s:
        # If the current character is not already present in the new string
        if char not in new_string:
            # Add the current character to the new string
            new_string += char

    return new_string
