
def return_n_smallest_chars(string):
    # Convert string to a list of characters
    char_list = list(string)
    # Sort the list in ascending order based on ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the top 37 characters from the sorted list
    return sorted_list[:37]
