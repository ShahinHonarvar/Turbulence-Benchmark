
def filter_chars(my_string):
    # Define the indices of the characters we want to remove
    start_index = 23
    end_index = 45
    # Create a new string to store the filtered characters
    filtered_string = ""

    # Iterate over each character in the original string
    for i, char in enumerate(my_string):
        # If the current character is between the indices we want to remove, skip it
        if start_index <= i < end_index:
            continue

        # Otherwise, append the character to the filtered string
        filtered_string += char

    return filtered_string
