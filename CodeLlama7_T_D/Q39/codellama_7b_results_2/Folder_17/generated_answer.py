
def return_n_greatest_chars(input_string):
    # Sort the input string in descending order based on ASCII values
    sorted_list = sorted(input_string, key=lambda x: ord(x), reverse=True)
    # Return the top 11 characters of the sorted list
    return sorted_list[:11]
