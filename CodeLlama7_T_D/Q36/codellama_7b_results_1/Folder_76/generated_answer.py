
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Iterate through the list of characters and remove any that fall between indices 669 and 888 (both exclusive)
    for i in range(len(char_list)):
        if 669 < i < 888:
            char_list.pop(i)
    # Join the list of characters back into a string and return it
    filtered_string = "".join(char_list)
    return filtered_string
