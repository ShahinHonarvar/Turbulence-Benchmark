
def return_n_greatest_chars(string, n=45):
    char_list = list(string)
    # Sort the characters in descending order based on their ASCII values
    char_list.sort(key=ord, reverse=True)
    # Return the top 45 characters from the sorted list
    return char_list[:n]
