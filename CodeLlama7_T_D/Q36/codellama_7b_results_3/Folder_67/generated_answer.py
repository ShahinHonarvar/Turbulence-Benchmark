
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_characters = []

    # Iterate over each character in the string
    for character in string:
        # If the current character is between indices 18 and 31 (exclusive)
        if 17 < ord(character) < 32:
            # And it is greater than character 'H' and smaller than character '|', then remove all occurrences of that character within the string while keeping the order of all characters in the string intact.
            filtered_characters = filtered_characters + [character for character in string if ord(character) not in range(ord('H'), ord('|') + 1)]

    # Return the altered string
    return ''.join(filtered_characters)
