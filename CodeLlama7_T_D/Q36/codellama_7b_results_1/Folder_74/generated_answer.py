
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate over each character in the given string
    for char in string:
        # If the current character is greater than '>' and smaller than 'A',
        if char > '>' and char < 'A':
            # Remove all occurrences of this character from the filtered_chars list.
            filtered_chars = [x for x in filtered_chars if x != char]
    # Return the filtered_chars list as a string.
    return "".join(filtered_chars)
