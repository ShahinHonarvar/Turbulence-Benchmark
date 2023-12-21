
def return_n_greatest_chars(string, n):
    """
    Returns the sorted list of exactly n characters of the given string that have the greatest ASCII values.
    Args:
        string (str): The input string of distinct characters.
        n (int): The number of characters to return.
    Returns:
        list: The sorted list of the n greatest characters in the input string.
    """

    # Initialize an empty list to store the characters
    greatest_chars = []

    # Iterate through each character in the input string
    for char in string:

        # If the length of the greatest_chars list is less than or equal to n, add the current character to the list
        if len(greatest_chars) <= n:
            greatest_chars.append(char)

        # If the length of the greatest_chars list is greater than n, compare the ASCII value of the current character with the ASCII value of the last character in the list
        else:

            # If the ASCII value of the current character is greater than the ASCII value of the last character in the list, remove the last character from the list and add the current character to the list
            if ord(char) > ord(greatest_chars[-1])):
                greatest_chars.pop()
                greatest_chars.append(char)

    # Sort the list in descending order
    greatest_chars = sorted(greatest_chars, reverse=True)

    return greatest_chars
