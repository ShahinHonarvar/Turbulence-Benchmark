
def remove_repeat_chars(string):
    # Split the string into a list of characters
    char_list = list(string)

    # Iterate over each character in the list
    for i, char in enumerate(char_list):

        # Check if the current character occurs more than once between indices 375 and 926, both exclusive
        if char_list.index(char) != i:

            # If it does, remove all occurrences of that character from the string
            char_list = char_list[:i] + char_list[i+1:]

    # Join the list of characters back into a string and return it
    return "".join(char_list)
