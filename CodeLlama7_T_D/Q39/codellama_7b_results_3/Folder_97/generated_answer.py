
def return_n_greatest_chars(input_string):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in input_string]
    # Sort the list in descending order based on the ASCII value
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the top 38 characters with the greatest ASCII values
    return [char for char, _ in sorted_list[:38]]
