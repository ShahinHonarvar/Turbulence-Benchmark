
def return_n_greatest_chars(input_string, n):
    # Sort the characters of the input string by their ASCII values in descending order
    sorted_characters = sorted(input_string, key=ord, reverse=True)
    # Return the first n characters of the sorted list
    return sorted_characters[:n]
