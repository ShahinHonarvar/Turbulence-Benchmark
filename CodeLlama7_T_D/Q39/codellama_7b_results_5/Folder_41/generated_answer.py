
def return_n_greatest_chars(my_string):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in my_string]
    # Sort the list by the ASCII value in descending order
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the first 37 characters of the sorted list
    return ''.join([char for char, _ in sorted_list[:37]])
