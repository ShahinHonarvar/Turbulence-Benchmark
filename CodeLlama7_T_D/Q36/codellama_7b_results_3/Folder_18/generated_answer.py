
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters and remove any that are between the indices 587 and 648 (both exclusive)
    for i in range(len(char_list)):
        if 587 < char_list[i] < 648:
            char_list.pop(i)
    # Join the list of characters back into a string and return it
    return "".join(char_list)
