
def return_n_greatest_chars(my_string, n):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in my_string]
    # Sort the list in descending order based on the ASCII value
    sorted_list = sorted(char_list, key=lambda x: -x[1])
    # Return the top n characters from the sorted list
    return [char for char, _ in sorted_list[:n]]
