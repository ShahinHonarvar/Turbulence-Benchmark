
def return_n_greatest_chars(string):
    # Sort the characters in the string based on their ASCII values
    sorted_characters = sorted(string, key=ord)

    # Return the top 38 characters of the sorted list
    return sorted_characters[-38:]
