
def return_n_greatest_chars(string):
    char_list = list(set(string))  # create a set of distinct characters from the string
    sorted_list = sorted(char_list, key=ord)  # sort the list in descending order using the ord function
    return sorted_list[:38]  # return the first 38 elements of the sorted list
