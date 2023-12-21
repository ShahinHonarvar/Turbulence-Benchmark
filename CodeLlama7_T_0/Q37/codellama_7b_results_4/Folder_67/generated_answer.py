
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 19 and 22, both inclusive
        if (i >= 19 and i <= 22) and (char_list[i] >= ']' and char_list[i] <= 't'):
            # Remove all occurrences of the current character from the list
            while char_list.count(char_list[i]) > 0:
                char_list.remove(char_list[i])
    # Join the characters in the list back into a string
    filtered_string = "".join(char_list)
    return filtered_string
