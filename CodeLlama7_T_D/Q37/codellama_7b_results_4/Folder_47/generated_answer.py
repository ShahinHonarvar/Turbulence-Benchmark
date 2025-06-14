
def filter_chars(string):
    # Create a new empty string
    filtered_string = ""

    # Iterate through each character in the given string
    for char in string:
        # If the current character is between indices 38 and 54, both inclusive, and is greater than or equal to character ':' and smaller than or equal to character 'r', then remove all occurrences of that character from the string
        if 37 < len(filtered_string) < 55 and char >= ":" and char <= "r":
            filtered_string = filtered_string.replace(char, "")
        else:
            # Otherwise, append the current character to the filtered string
            filtered_string += char

    # Return the altered string
    return filtered_string
