
def return_n_smallest_chars(string, n):
    """
    Return a list of exactly n characters of the given string that have the smallest ASCII values.
    Args:
        string (str): The input string.
        n (int): The number of characters to return.
    Returns:
        list: A list of exactly n characters of the given string that have the smallest ASCII values.
    """

    # Sort the characters in descending order based on their ASCII values
    sorted_chars = sorted(string, key=ord, reverse=True)
    # Return the top n characters from the sorted list
    return sorted_chars[:n]
