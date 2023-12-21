
def return_n_greatest_chars(my_string, n):
    # create a list of characters from the input string
    char_list = list(my_string)
    # sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # return the top 'n' characters from the sorted list
    return sorted_list[:n]
