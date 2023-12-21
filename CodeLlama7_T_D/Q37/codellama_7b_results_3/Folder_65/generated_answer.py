
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 61 and 70, both inclusive
        if (i >= 61 and i <= 70):
            # Check if the current character is greater than or equal to character '0' and smaller than or equal to character '@'
            if (char_list[i] >= '0' and char_list[i] <= '@'):
                # Remove all occurrences of the current character from the string
                char_list.remove(char_list[i])
    # Join the list of characters back into a single string
    filtered_string = "".join(char_list)
    return filtered_string
