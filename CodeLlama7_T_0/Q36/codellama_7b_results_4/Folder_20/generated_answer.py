
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters in the list
    for i in range(13, 40):
        # Check if the current character is greater than ':' and smaller than 'C'
        if char_list[i] > ':' and char_list[i] < 'C':
            # Remove all occurrences of the current character from the list
            while char_list[i] in char_list:
                char_list.remove(char_list[i])
    # Join the characters in the list back into a string
    filtered_string = "".join(char_list)
    return filtered_string
