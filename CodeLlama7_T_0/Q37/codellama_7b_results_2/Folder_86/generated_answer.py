
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 164 and 706, both inclusive
        if (i >= 164 and i <= 706) and (char_list[i] >= 'O' and char_list[i] <= '}'):
            # Remove all occurrences of the current character from the list
            while char_list.count(char_list[i]) > 1:
                char_list.remove(char_list[i])
    # Join the characters in the list back into a string
    filtered_string = "".join(char_list)
    return filtered_string
