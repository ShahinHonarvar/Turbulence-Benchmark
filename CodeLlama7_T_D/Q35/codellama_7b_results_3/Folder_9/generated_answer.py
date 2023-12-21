
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set(s)
    # Initialize an empty string to store the altered string
    altered_string = ""
    # Iterate through each character in the string
    for char in s:
        # If the character is not in the set of unique characters, append it to the altered string
        if char not in unique_chars:
            altered_string += char

    # Return the altered string
    return altered_string
