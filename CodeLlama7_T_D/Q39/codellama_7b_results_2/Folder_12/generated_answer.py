
def return_n_greatest_chars(my_string):
    # sort the string in descending order based on ASCII values
    sorted_list = sorted(my_string, key=ord, reverse=True)
    # return the first 61 characters of the sorted list
    return sorted_list[:61]
