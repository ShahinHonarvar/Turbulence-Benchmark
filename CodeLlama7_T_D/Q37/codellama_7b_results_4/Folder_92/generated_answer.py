
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 4 and 4, both inclusive, and is greater than or equal to character '7' and smaller than or equal to character 'o'
        if (char >= "7" and char <= "o") and (len(string) - 1) >= char:
            # If the current character meets the condition above, remove all occurrences of that character from the string
            filtered_string = filtered_string.replace(char, "")

        # Add the current character to the filtered string
        filtered_string += char

    # Return the altered string
    return filtered_string
