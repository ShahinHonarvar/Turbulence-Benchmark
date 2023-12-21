
def filter_chars(my_string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in my_string:

        # If the character is between indices 672 and 709 (exclusive) and is greater than 'X' and smaller than '}', remove all occurrences of that character within the string while keeping the order of all characters intact.
        if (char >= my_string[672] and char <= my_string[709]) and (char > 'X' and char < '}'):
            # Remove all occurrences of the current character from the filtered list
            filtered_chars = [c for c in filtered_chars if c != char]

    # Return the altered string with the filtered characters removed
    return "".join(filtered_chars)
