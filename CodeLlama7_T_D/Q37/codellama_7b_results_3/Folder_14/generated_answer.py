
def filter_chars(my_string):
    # Create a list of all characters in the string
    char_list = list(my_string)
    # Loop through each character and check if it meets the criteria
    for i in range(len(char_list)):
        if (char_list[i] >= 'A' and char_list[i] <= 'b') and (i >= 35 and i <= 98):
            # If the character meets the criteria, remove it from the list
            char_list.pop(i)
    # Join the modified list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
