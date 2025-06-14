
def return_n_greatest_chars(input_string, n):
    # Create a list of tuples containing the character and its ASCII value
    char_ascii_list = [(char, ord(char)) for char in input_string]
    # Sort the list by the second element (ASCII value) in descending order
    sorted_list = sorted(char_ascii_list, key=lambda x: x[1], reverse=True)
    # Return the first n elements of the sorted list
    return [char for char, _ in sorted_list[:n]]
