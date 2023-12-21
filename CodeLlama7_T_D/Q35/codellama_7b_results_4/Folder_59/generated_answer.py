
def remove_repeat_chars(s):
    # Initialize an empty list to store the characters of the string
    chars = []

    # Iterate through each character in the given string
    for char in s:

        # If the current character is not already in the list of characters, add it to the list
        if char not in chars:
            chars.append(char)

    # Initialize an empty string to store the altered string
    result = ""

    # Iterate through each character in the list of characters
    for char in chars:

        # If the current character is not repeated in the given string, add it to the altered string
        if s.count(char) == 1:
            result += char

    # Return the altered string
    return result
