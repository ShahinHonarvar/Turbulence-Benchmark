
def return_n_greatest_chars(input_string):
    # Create a list of all characters in the input string
    char_list = list(input_string)

    # Sort the list in descending order based on ASCII values

    sorted_char_list = sorted(char_list, key=ord, reverse=True)

    # Return the top 45 characters of the sorted list

    return sorted_char_list[:45]
