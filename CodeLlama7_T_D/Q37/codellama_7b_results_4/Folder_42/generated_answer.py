
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over the characters in the original string
    for char in s:
        # Check if the character is between indices 73 and 74, both inclusive, and is greater than or equal to character 'U' and smaller than or equal to character 'l'
        if (73 <= ord(char) <= 74) and ('U' <= char <= 'l'):
            # If the character is between these indices and meets the condition, skip it
            continue

        # Otherwise, add the character to the filtered string
        filtered += char

    # Return the filtered string
    return filtered
