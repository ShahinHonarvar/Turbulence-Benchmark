
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Iterate over each character in the list and check if it satisfies the condition
    for i in range(len(char_list)):
        if (char_list[i] >= '/') and (char_list[i] <= '8'):
            char_list.pop(i)
    # Return the altered string by joining the list of characters back together
    return "".join(char_list)
