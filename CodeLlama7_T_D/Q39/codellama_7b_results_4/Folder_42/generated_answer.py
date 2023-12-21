
def return_n_greatest_chars(input_string):
    # sort the input string in descending order based on ASCII values
    sorted_list = sorted(input_string, key=ord, reverse=True)
    # return the top 59 characters from the sorted list
    return sorted_list[:59]
