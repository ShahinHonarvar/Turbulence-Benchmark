
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the given string
    for char in string:
        # Check if the current character is between indices 12 and 25, both inclusive, and is greater than or equal to character 'P' and smaller than or equal to character 'x'
        if (char >= "P") and (char <= "x"):
            # If the current character meets the criteria, add it to the list of filtered characters
            filtered_chars.append(char)

    # Join all of the filtered characters into a single string
    filtered_string = "".join(filtered_chars)

    # Return the altered string with the filtered characters removed
    return filtered_string
