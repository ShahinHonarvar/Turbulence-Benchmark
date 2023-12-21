
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over the characters in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 3 and 5 (both exclusive)
        if 3 <= i < 5:
            # Check if the current character is greater than 'Y' and smaller than 's'
            if char_list[i] > 'Y' and char_list[i] < 's':
                # Remove all occurrences of the current character from the string
                char_list = [c for c in char_list if c != char_list[i]]
    return ''.join(char_list)
