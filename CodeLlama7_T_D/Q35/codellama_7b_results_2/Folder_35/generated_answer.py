 def remove_repeat_chars(s):
    # Create a new string with the modified characters
    new_string = ""

    # Loop through each character in the input string
    for char in s:

        # If the current character is not already in the new string, add it to the end of the new string
        if char not in new_string:
            new_string += char

    # Return the altered string
    return new_string
