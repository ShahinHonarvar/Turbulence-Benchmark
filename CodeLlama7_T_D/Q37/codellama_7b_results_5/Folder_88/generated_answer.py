
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_characters = []

    # Iterate over each character in the given string
    for character in string:

        # If the current character is between indices 69 and 80, both inclusive, and is greater than or equal to '@' and smaller than or equal to 'p', then remove all occurrences of that character from the string
        if (character >= '@') and (character <= 'p')):
            filtered_characters.append(character)

    # Return the altered string with the filtered characters removed
    return ''.join(filtered_characters))
