
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over the characters of the given string
    for char in s:
        # Check if the current character is between indices 35 and 40, both inclusive, and is greater than or equal to character ')' and smaller than or equal to character 'l'
        if (char >= ")" and char <= "l") and (char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u"):
            # If the current character meets the above condition, append it to the filtered string
            filtered += char

    # Return the altered string containing only the filtered characters
    return filtered
