
def return_n_greatest_chars(input_string):
    # Convert the input string to a list of characters
    input_list = list(input_string)

    # Sort the list in descending order based on the ASCII values of the characters
    sorted_list = sorted(input_list, key=ord, reverse=True)

    # Return the top 20 elements of the sorted list
    return sorted_list[:20]
