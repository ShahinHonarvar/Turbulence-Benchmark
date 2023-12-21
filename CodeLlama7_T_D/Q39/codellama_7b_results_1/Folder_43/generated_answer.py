
def return_n_greatest_chars(input_string):
    # sort the characters in descending order based on their ASCII values
    sorted_list = sorted(input_string, key=ord, reverse=True)
    # return the top 56 characters from the sorted list
    return sorted_list[:56]
