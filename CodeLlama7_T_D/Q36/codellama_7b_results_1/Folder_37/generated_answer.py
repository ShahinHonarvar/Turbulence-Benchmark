
def filter_chars(my_string):
    # Create a list of characters in the string
    char_list = list(my_string)
    # Iterate over the characters and remove those that match the criteria
    for i in range(len(char_list)):
        if char_list[i] > '/' and char_list[i] < '6':
            char_list.pop(i)
            # Decrement the iterator to account for the removed character
            i -= 1

    # Join the list of characters back into a string
    filtered_string = "".join(char_list)
    return filtered_string
