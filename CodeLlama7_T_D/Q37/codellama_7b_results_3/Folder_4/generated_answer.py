 def filter_chars(string):
    # Create a list of characters from the given string
    char_list = list(string)
    # Iterate through the characters and remove any that do not meet the criteria
    for i in range(19, 34):
        if char_list[i] < 'S' or char_list[i] > '{':
            char_list.pop(i)
    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
