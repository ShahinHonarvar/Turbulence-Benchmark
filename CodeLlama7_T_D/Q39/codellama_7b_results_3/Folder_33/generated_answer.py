 def return_n_greatest_chars(string):
    """
    A function that takes a string of distinct characters and creates the sorted list of exactly 36 characters of the given string that have the greatest ASCII values. The function should sort the list in descending order and returns it.
    Args:
        string (str): A string of distinct characters.
    Returns:
        list: A list of exactly 36 characters of the given string that have the greatest ASCII values, sorted in descending order.
    """

    # Initialize an empty list to store the sorted characters
    sorted_chars = []

    # Loop through each character in the input string
    for char in string:

        # If the current character is not already in the sorted list, add it
        if char not in sorted_chars:
            sorted_chars.append(char)

    # Sort the list of characters in descending order based on their ASCII values
    sorted_chars.sort(key=ord, reverse=True)

    # Return the first 36 characters of the sorted list
    return sorted_chars[:36]
