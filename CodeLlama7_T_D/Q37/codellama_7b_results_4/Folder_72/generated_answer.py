
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Loop through the characters and remove any that are not within the desired range
    for i, char in enumerate(char_list):
        if i < 35 or i > 51:
            continue

        elif char < 'H' or char > 's':
            char_list.remove(char)

    # Join the list of characters back into a string and return it
    return "".join(char_list)
