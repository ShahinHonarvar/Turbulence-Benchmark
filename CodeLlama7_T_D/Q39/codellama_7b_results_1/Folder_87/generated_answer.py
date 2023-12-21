
def return_n_greatest_chars(my_string, n):
    # Create a list of all characters in the string
    char_list = list(my_string)

    # Sort the list in descending order based on ASCII values

    char_list.sort(key=ord, reverse=True)

    # Return the top n characters from the sorted list

    return char_list[:n]
