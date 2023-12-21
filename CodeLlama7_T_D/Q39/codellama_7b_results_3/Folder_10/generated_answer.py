
def return_n_greatest_chars(input_string, n):
    char_list = list(input_string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 'n' characters from the sorted list
    return sorted_list[:n]
