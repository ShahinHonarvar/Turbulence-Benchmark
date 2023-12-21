
def filter_chars(my_string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the input string
    for char in my_string:
        # If the current character is between the indices 38 and 81 (both exclusive)
        if 37 < ord(char) < 82:
            # Remove all occurrences of this character from the filtered characters list
            filtered_chars = [c for c in filtered_chars if c != char]
        # Otherwise, add the current character to the filtered characters list
        else:
            filtered_chars.append(char)

    # Join all the filtered characters together into a single string
    filtered_string = "".join(filtered_chars)

    # Return the altered string with the filtered characters removed
    return filtered_string
