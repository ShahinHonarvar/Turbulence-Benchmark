
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set()
    # Initialize an empty string to store the altered string
    altered_string = ""
    # Iterate through each character in the string
    for char in s:
        # If the character is not already in the set of unique characters, add it
        if char not in unique_chars:
            # Add the character to the set of unique characters
            unique_chars.add(char)
            # Append the character to the altered string
            altered_string += char

    # Return the altered string
    return altered_string
