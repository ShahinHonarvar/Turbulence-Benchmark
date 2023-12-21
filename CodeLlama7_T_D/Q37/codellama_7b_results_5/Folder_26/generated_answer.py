
def filter_chars(string):
    # Split the string into a list of characters
    char_list = list(string)
    # Iterate over the list of characters
    for i in range(len(char_list)):
        # Get the current character and its index
        curr_char = char_list[i]
        curr_index = i
        # Check if the current character is between indices 20 and 62, both inclusive
        if (curr_index >= 20) and (curr_index <= 62):
            # Check if the current character satisfies the condition
            if (curr_char >= 'i') and (curr_char <= 'k'):
                # Remove all occurrences of the current character from the string
                char_list.remove(curr_char)
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
