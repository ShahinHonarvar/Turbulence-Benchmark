
def return_n_greatest_chars(string, n):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in string]
    # Sort the list by the ASCII value in descending order
    char_list.sort(key=lambda x: x[1], reverse=True)
    # Return the top n characters from the sorted list
    return [char for char, _ in char_list[:n]]
