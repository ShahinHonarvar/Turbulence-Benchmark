
def return_n_greatest_chars(input_str, n=87):
    """
    Return the sorted list of exactly n characters of the given string that have the greatest ASCII values.
    Parameters:
        input_str (string): The string to be processed.
        n (integer, optional): The number of characters to return. Defaults to 87.
    Returns:
        A list of exactly n characters from the given string sorted in descending order based on their ASCII values.
    """

    # Initialize an empty list to store the sorted characters
    sorted_chars = []

    # Iterate through each character in the input string
    for char in input_str:

        # If the number of characters in the sorted list is less than or equal to n, add the current character to the sorted list
        if len(sorted_chars) <= n:
            sorted_chars.append(char)

        # Else, sort the list based on the ASCII values of the characters and return the first n elements of the sorted list
        else:
            break

    # Sort the list of characters in descending order based on their ASCII values
    sorted_chars = sorted(sorted_chars, key=ord, reverse=True)

    # Return the first n elements of the sorted list of characters
    return sorted_chars[:n]
