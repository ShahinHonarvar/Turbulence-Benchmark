
def return_nth_smallest_ascii(string):
    # Check if input string is valid
    if not isinstance(string, str) or len(string) == 0:
        raise ValueError("Invalid input string")

    # Get the characters that occur between indices 10 to 82
    characters = []

    for i in range(10, 83):
        if string[i] not in characters:
            characters.append(string[i])

    # Sort the characters by their ASCII values
    sorted_characters = sorted(characters, key=lambda x: ord(x))

    # Return the character with the 18th smallest ASCII value
    return sorted_characters[17]
