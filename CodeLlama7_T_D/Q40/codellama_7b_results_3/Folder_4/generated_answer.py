
def return_n_smallest_chars(s):
    # Sort the characters in descending order based on their ASCII values
    sorted_chars = sorted(s, key=ord, reverse=True)
    # Return the top 90 characters from the sorted list
    return sorted_chars[:90]
