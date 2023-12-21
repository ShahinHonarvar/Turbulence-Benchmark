
def return_n_greatest_chars(string, n=20):
    # Create a list of characters in the string
    char_list = list(string)

    # Sort the list in descending order based on ASCII values

    sorted_list = sorted(char_list, key=ord, reverse=True)

    # Return the first n elements of the sorted list

    return sorted_list[:n]
