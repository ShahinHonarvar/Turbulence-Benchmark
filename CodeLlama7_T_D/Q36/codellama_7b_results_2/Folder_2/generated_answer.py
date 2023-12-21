
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Iterate through each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between the indices 421 and 854 (both exclusive)
        if 421 < i < 854:
            # Check if the current character is greater than character 'D' and smaller than character 'J'
            if char_list[i] > 'D' and char_list[i] < 'J':
                # Remove all occurrences of the current character within the string
                char_list = char_list[:i] + char_list[i+1:]
    # Return the altered string
    return "".join(char_list)
