
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Iterate over the characters and remove any that fall within the specified range
    for i, char in enumerate(char_list):
        if 66 <= ord(char) <= 90:
            char_list.remove(char)
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
