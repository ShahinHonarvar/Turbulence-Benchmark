
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 14 and 75 (both exclusive)
        if 14 < i < 75:
            # Check if the current character is greater than '9' and smaller than 'K'
            if char_list[i] > '9' and char_list[i] < 'K':
                # Remove all occurrences of the current character from the list
                while char_list[i] in char_list:
                    char_list.remove(char_list[i])

    # Join the characters in the list back into a string
    filtered_string = "".join(char_list)

    return filtered_string
