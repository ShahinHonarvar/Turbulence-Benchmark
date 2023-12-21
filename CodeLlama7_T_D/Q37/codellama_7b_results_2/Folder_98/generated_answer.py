
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over the characters in the given string
    for char in s:

        # If the current character is between indices 8 and 9, both inclusive, and is greater than or equal to character 'R' and smaller than or equal to character 't', then remove all occurrences of that character from the filtered string
        if (8 <= ord(char) <= 9) and ('R' <= char <= 't'):
            continue

        # Otherwise, add the current character to the filtered string
        else:
            filtered += char

    # Return the altered string containing only the filtered characters
    return filtered
