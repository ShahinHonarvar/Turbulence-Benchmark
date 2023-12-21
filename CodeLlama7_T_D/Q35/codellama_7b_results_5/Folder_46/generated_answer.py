
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    unique_chars = set(s)
    # Initialize an empty string to store the altered string
    altered_string = ""

    # Iterate over each character in the string
    for char in s:
        # If the current character is not in the set of unique characters, append it to the altered string
        if char not in unique_chars:
            altered_string += char

        # If the current character is in the set of unique characters and its index is greater than or equal to 10 and less than or equal to 79, remove all occurrences of that character from the string
        elif s.index(char) >= 10 and s.index(char) <= 79:
            altered_string += char

    # Return the altered string
    return altered_string
