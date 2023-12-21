
def filter_chars(s):
    # Create a list of characters from the given string
    char_list = list(s)
    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # If the current character is between 55 and 66 (exclusive)
        if char_list[i] > 'f' and char_list[i] < '|':
            # Remove all occurrences of this character from the list
            while char_list[i] in char_list:
                char_list.remove(char_list[i])
    # Join the characters back into a string
    return ''.join(char_list)
