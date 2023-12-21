
def return_n_greatest_chars(s, n):
    """
    Returns the sorted list of exactly n characters
    of the given string that have the greatest ASCII values.

    Args:
        s (string): The input string.
        n (int): The number of characters to return.

    Returns:
        list: The sorted list of exactly n characters of the given string that have the greatest ASCII values.

    """

    if len(s) < n:
        raise ValueError("Input string is shorter than the specified number of characters")

    chars = []

    for i in range(n):

        char = s[i]

        if char in chars:
            continue

        else:
            chars.append(char)

    return sorted(chars, key=ord, reverse=True)
