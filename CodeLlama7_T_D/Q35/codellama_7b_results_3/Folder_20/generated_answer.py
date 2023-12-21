
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set(s)
    # Initialize an empty string to store the altered string
    altered_string = ""

    for char in s:
        if char not in unique_chars:
            # If the current character is not already in the altered string, append it
            altered_string += char

            # Add the current character to the set of unique characters
            unique_chars.add(char)

    return altered_string
