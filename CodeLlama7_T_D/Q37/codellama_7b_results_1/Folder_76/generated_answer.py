
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Iterate through the list and remove any characters that do not meet the specified criteria
    for i in range(len(char_list)):
        if (char_list[i] < 'M' or char_list[i] > 'v') and i >= 379 and i <= 898:
            char_list.pop(i)
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
