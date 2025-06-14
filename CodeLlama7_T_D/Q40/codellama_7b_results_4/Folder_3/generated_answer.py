
def return_n_smallest_chars(string, n=28):
    # Sort the characters in descending order based on their ASCII values
    sorted_chars = sorted(string, key=ord, reverse=True)
    # Return the top n characters from the sorted list
    return sorted_chars[:n]
