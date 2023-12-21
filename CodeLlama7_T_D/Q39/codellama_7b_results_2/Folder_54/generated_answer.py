
def return_n_greatest_chars(string, n=79):
    """
    Returns the sorted list of exactly n characters of the given string that have the greatest ASCII values. The function should sort the list in descending order and returns it.
    Args:
        string (str): String of distinct characters
        n (int, optional): Number of characters to return. Defaults to 79.
    Returns:
        list: Sorted list of exactly n characters of the given string that have the greatest ASCII values.
    """

    # Create a dictionary with the character as key and its ASCII value as value
    char_ascii = {char:ord(char) for char in string}

    # Sort the dictionary by value in descending order
    sorted_dict = sorted(char_ascii.items(), key=lambda x:x[1], reverse=True)

    # Return the first n characters of the sorted list
    return [char for char, _ in sorted_dict[:n]]
