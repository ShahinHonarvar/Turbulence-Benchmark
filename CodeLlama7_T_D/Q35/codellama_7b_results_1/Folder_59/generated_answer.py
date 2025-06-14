
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set(s)
    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the string
    for char in s:
        # If the character is not in the set of unique characters, add it to the result string
        if char not in unique_chars:
            result += char

        # Add the character to the set of unique characters
        unique_chars.add(char)

    # Return the altered string
    return result
