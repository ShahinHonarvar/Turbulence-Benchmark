
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 36 and 40, both inclusive
        if (i >= 36 and i <= 40) and (char_list[i] >= 'H' and char_list[i] <= 'e'):
            # Remove all occurrences of this character from the list
            while char_list.count(char_list[i]) > 1:
                char_list.remove(char_list[i])
    # Join the characters in the list back into a string
    new_string = "".join(char_list)
    return new_string
