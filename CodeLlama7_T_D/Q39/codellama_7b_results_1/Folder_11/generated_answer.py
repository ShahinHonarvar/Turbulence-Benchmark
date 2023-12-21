
def return_n_greatest_chars(input_string):
    # Sort the input string in descending order based on ASCII values
    sorted_list = sorted(input_string, key=ord, reverse=True)
    # Return the top 17 characters from the sorted list
    return sorted_list[:17]
