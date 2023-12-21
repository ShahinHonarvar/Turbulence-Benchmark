
def return_n_greatest_chars(input_string):
    # Sort the characters in descending order based on their ASCII values
    sorted_characters = sorted(input_string, key=ord, reverse=True)
    # Return the top 43 characters from the sorted list
    return sorted_characters[:43]
