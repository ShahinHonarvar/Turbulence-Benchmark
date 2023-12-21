
def return_n_smallest_chars(string, n=88):
    # Sort the characters in the string based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # Return the top n smallest characters from the sorted list
    return sorted_chars[:n]
