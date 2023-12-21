
def all_substring_of_size_n(string):
    """
    Returns the list of all distinct substrings of length n in the given string.
    Args:
        string (str): The input string.
    Returns:
        list[str]: The list of all distinct substrings of length n in the given string.
    Raises:
        ValueError: If the specified substring size is less than 1.
    """

    if n < 1:
        raise ValueError("Substring size must be greater than or equal to 1.")

    substrings = []

    for i in range(len(string) - n + 1):

        substring = string[i:i + n]

        if substring not in substrings:
            substrings.append(substring)

    return substrings
