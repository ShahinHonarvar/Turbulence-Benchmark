
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over each character in the list
    for i, char in enumerate(char_list):
        # Check if the current character is between indices 2 and 7 (both exclusive)
        if 2 <= i < 7:
            # Check if the current character is greater than 'h' and smaller than 'k'
            if char > 'h' and char < 'k':
                # Remove all occurrences of this character from the list
                while True:
                    try:
                        char_list.remove(char)
                    except ValueError:
                        break

    # Join the remaining characters in the list into a string
    filtered_string = ''.join(char_list)
    return filtered_string
