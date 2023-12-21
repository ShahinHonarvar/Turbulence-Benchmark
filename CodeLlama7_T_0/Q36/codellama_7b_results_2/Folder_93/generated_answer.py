
def filter_chars(my_string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate through each character in the string
    for char in my_string:
        # If the current character is between the indices 52 and 88 (both exclusive) and it is greater than '&' and smaller than 'c', then remove all occurrences of that character within the string while keeping the order of all characters intact.
        if char in range(52, 88) and char > '&' and char < 'c':
            # Replace all occurrences of the current character with an empty string
            my_string = my_string.replace(char, '')

    # Return the altered string
    return my_string
