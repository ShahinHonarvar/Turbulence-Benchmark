
def remove_repeat_chars(string):
    # Create a set of unique characters in the string
    unique_chars = set(string)
    # Initialize an empty string
    altered_string = ""

    # Iterate through each character in the string
    for char in string:
        # If the character is not in the set of unique characters, add it to the altered string
        if char not in unique_chars:
            altered_string += char

    return altered_string
