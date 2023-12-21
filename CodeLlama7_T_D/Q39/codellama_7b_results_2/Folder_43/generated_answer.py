
def return_n_greatest_chars(input_string, n=56):
    char_list = list(input_string)
    # sort the character list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # return the top 56 characters of the sorted list
    return sorted_list[:n]
