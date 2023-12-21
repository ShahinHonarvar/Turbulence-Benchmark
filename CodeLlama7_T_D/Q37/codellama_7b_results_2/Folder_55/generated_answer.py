
def filter_chars(my_string):
    # Create a list of characters from the given string
    char_list = list(my_string)
    # Iterate over each character in the list and remove it if it meets the criteria
    for i, c in enumerate(char_list):
        if (c >= '$' and c <= ';') and (i > 0 and i < len(char_list) - 1):
            char_list.remove(c)
    # Join the list of characters back into a string
    altered_string = "".join(char_list)
    return altered_string
