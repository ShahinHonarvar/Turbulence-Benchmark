
def filter_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Iterate over each character in the string
    for i in range(len(char_list)):
        # Check if the current character is between indices 12 and 77, both inclusive
        if (i >= 12 and i <= 77):
            # Check if the current character is greater than or equal to character ':' and smaller than or equal to character 'L'
            if ((char_list[i] >= ':') and (char_list[i] <= 'L')):
                # Remove all occurrences of the current character from the string
                char_list.remove(char_list[i])
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
