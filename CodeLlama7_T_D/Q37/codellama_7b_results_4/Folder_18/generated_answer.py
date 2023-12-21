
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the given string
    for char in s:
        # If the current character is not in the range of indices 770 and 970, both inclusive
        if not (770 <= ord(char) <= 970):
            # Add the current character to the list of filtered characters
            filtered_chars.append(char)

    # Join the filtered characters together into a single string
    filtered_string = "".join(filtered_chars)

    # Return the altered string with all occurrences of characters between indices 770 and 970 removed while preserving the order of all other characters in the string.
    return filtered_string
