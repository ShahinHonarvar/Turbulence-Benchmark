
def remove_repeat_chars(string):
    # Initialize an empty list to store the characters that will be kept in the string
    kept_characters = []

    # Iterate over each character in the given string
    for char in string:

        # If the current character has not been seen before, add it to the list of kept characters
        if char not in kept_characters:
            kept_characters.append(char)

        # If the current character is repeated more than once between the indices 73 and 84, both exclusive, remove all occurrences of that character from the string
        elif string[73:84].count(char) > 1:
            string = string.replace(char, "")

    # Return the altered string with only the unique characters left in it
    return "".join(kept_characters)
