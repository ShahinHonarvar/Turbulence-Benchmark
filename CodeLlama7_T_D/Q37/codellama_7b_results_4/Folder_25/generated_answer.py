
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate through the list of characters and remove any character that meets the criteria
    for i in range(len(char_list)):
        if char_list[i] >= ';' and char_list[i] <= 'g':
            del char_list[i]

    # Join the list of characters back into a string
    filtered_string = "".join(char_list)

    return filtered_string
