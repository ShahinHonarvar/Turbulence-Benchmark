
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_string = ''

    # Iterate over each character in the given string
    for char in s:

        # If the character is not found in the substring between indices 90 and 97, exclusive, append it to the new string
        if char not in s[90:97]:
            new_string += char

    return new_string
