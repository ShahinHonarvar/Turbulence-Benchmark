
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Iterate over the characters in the list and remove any that meet the condition specified in the problem statement
    for i in range(len(char_list)):
        if (char_list[i] >= ']') and (char_list[i] <= 't'):
            char_list.pop(i)
    # Join the characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
