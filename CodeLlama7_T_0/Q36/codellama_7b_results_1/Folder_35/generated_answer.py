
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between 163 and 658 (exclusive)
        if 163 < char_list[i] < 658:
            # If it is, check if it is greater than '(' and smaller than ']'
            if char_list[i] > '(' and char_list[i] < ']':
                # If it is, remove all occurrences of that character in the string while keeping the order of all characters intact
                char_list = [char for char in char_list if char != char_list[i]]

    # Return the altered string
    return "".join(char_list)
