
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for char in s:
        # If the character is between indices 379 and 898, both inclusive, and is greater than or equal to 'M' and smaller than or equal to 'v', then remove all occurrences of that character from the string
        if (char >= "M" and char <= "v") and 379 <= s.index(char) <= 898:
            # Replace all occurrences of the current character with an empty string
            filtered = filtered.replace(char, "")

        # Otherwise, append the current character to the filtered string
        else:
            filtered += char

    # Return the filtered string
    return filtered
