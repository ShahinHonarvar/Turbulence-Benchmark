
def filter_chars(string):
    # Create a list of characters in the string
    char_list = list(string)
    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the character is between indices 19 and 22, both inclusive
        if (i >= 19 and i <= 22):
            # Check if the character is greater than or equal to ']' and smaller than or equal to 't'
            if (char_list[i] >= ']' and char_list[i] <= 't'):
                # Remove all occurrences of the character from the string
                char_list.remove(char_list[i])
    # Join the list of characters back into a string
    altered_string = "".join(char_list)
    return altered_string
