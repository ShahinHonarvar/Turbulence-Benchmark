
def return_n_greatest_chars(string):
    # Split the string into a list of individual characters
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the first 19 elements of the sorted list
    return sorted_list[:19]
