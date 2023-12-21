
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set(s)
    # Initialize an empty string to store the altered string
    altered_string = ""

    # Iterate over each character in the original string
    for char in s:
        # If the character is not in the set of unique characters, add it to the altered string and continue with the next character
        if char not in unique_chars:
            altered_string += char
            continue

        # If the character is already in the altered string, skip adding it again
        if char in altered_string:
            continue

        # Add the character to the altered string and continue with the next character
        altered_string += char

    # Return the altered string
    return altered_string
