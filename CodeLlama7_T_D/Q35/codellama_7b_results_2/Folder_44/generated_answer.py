
def remove_repeat_chars(string):
    # Create a set of unique characters in the string
    unique_chars = set(string)
    # Initialize an empty string to store the altered string
    altered_string = ""

    # Iterate through each character in the original string
    for char in string:
        # If the current character is not in the set of unique characters, append it to the altered string
        if char not in unique_chars:
            altered_string += char

    # Return the altered string
    return altered_string
