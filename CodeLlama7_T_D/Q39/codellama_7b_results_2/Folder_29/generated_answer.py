
def return_n_greatest_chars(string):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the top 23 characters of the sorted list
    return [item[0] for item in sorted_list[:23]]
