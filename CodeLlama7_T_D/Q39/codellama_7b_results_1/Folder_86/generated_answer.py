
def return_n_greatest_chars(input_string):
    # Split the input string into a list of individual characters
    char_list = list(input_string)

    # Sort the character list in descending order based on ASCII values
    char_list.sort(key=lambda x: ord(x), reverse=True)

    # Return the top 34 characters of the sorted list
    return char_list[:34]
