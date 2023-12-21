
def filter_chars(string):
    # Create a new list to store the filtered characters
    filtered_list = []

    # Iterate through each character in the string
    for char in string:

        # Check if the current character is between the indices 163 and 658 (both exclusive)
        if 163 < ord(char) < 658:

            # If the current character is a valid filtered character, add it to the filtered list
            filtered_list.append(char)

    # Return the altered string with the filtered characters
    return "".join(filtered_list)
