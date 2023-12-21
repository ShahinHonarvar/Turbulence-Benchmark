
def return_n_greatest_chars(string, n):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in string]
    # Sort the list by the ASCII value in descending order
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the first n elements of the sorted list
    return [element[0] for element in sorted_list[:n]]
