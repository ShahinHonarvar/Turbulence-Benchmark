
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 15 and 55, both inclusive
        if 15 <= i <= 55:
            # Check if the current character is greater than or equal to 'W' and smaller than or equal to '{', both inclusive
            if char_list[i] >= 'W' and char_list[i] <= '{':
                # Remove all occurrences of the current character from the string
                char_list.remove(char_list[i])
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
