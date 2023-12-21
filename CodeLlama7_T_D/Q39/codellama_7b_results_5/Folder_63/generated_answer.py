
def return_n_greatest_chars(input_string):
    # create a list of characters from the input string
    char_list = list(input_string)
    # sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # return the top 44 characters from the sorted list
    return char_list[:44]
