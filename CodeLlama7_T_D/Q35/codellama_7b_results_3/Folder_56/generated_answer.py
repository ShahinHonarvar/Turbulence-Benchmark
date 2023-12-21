
def remove_repeat_chars(string):
    # Create a list of characters from the given string
    char_list = list(string)

    # Iterate over each character in the list
    for char in char_list:

        # Check if the current character occurs more than once between indices 7 and 9
        if char_list.count(char) > 1 and (char_list.index(char) >= 7 and char_list.index(char) < 9)):

            # Remove all occurrences of the current character from the list
            while char in char_list:
                char_list.remove(char)

    # Join the remaining characters in the list into a string
    return "".join(char_list)
