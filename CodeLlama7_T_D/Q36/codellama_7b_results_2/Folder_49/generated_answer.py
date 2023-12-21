
def filter_chars(string):
    # Define the range of characters to remove
    remove_range = range(46, 91)
    # Initialize an empty string to store the filtered result
    filtered_string = ""
    # Iterate over each character in the input string
    for char in string:
        # If the current character is within the range of characters to remove, skip it
        if ord(char) in remove_range:
            continue

        # Otherwise, append the current character to the filtered result
        filtered_string += char

    return filtered_string
