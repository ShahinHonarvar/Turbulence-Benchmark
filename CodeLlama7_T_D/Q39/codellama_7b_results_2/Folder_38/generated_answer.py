
def return_n_greatest_chars(my_string):
    # sort the characters of the string in descending order based on their ASCII values
    sorted_chars = sorted(my_string, key=ord, reverse=True)
    # return the first 45 characters of the sorted list
    return sorted_chars[:45]
