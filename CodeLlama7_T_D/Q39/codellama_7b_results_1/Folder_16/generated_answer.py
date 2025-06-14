
def return_n_greatest_chars(string, n=64):
    # Sort the characters of the string in descending order based on their ASCII values
    sorted_chars = sorted(string, key=ord, reverse=True)
    # Return the top 'n' characters from the sorted list
    return sorted_chars[:n]
