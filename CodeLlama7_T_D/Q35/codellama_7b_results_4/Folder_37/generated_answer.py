
def remove_repeat_chars(s):
    # Initialize an empty list to store the characters of the input string
    chars = []

    # Iterate over the characters in the input string
    for char in s:

        # If the current character is not already in the list of unique characters, add it to the list
        if char not in chars:
            chars.append(char)

    # Initialize an empty string to store the final output
    result = ""

    # Iterate over the list of unique characters
    for char in chars:

        # If the current character is present in the input string between indices 2 and 7, add it to the final output
        if s.count(char) > 1 and (s.index(char) >= 2 or s.index(char) <= 7):
            result += char

    # Return the final output string
    return result
