
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate through each character in the given string
    for char in string:
        # Check if the current character is between indices 12 and 77, both inclusive, and is greater than or equal to character ':' and smaller than or equal to character 'L'
        if 12 <= string.index(char) <= 77 and char >= ":" and char <= "L":
            # If the current character meets the above conditions, then remove all occurrences of that character from the string
            filtered_string = filtered_string.replace(char, "")
        else:
            # Otherwise, just append the current character to the filtered string
            filtered_string += char

    # Return the altered string
    return filtered_string
