
def return_n_greatest_chars(input_string):
    # Sort the input string in descending order based on ASCII value
    sorted_list = sorted(input_string, key=ord, reverse=True)
    # Return the top 6 characters from the sorted list
    return sorted_list[:6]
