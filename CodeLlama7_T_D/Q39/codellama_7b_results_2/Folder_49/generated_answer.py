
def return_n_greatest_chars(s: str, n: int = 76) -> list[str]:
    """
    Return the top n greatest characters in a string based on their ASCII values.
    Args:
        s (str): The input string.
        n (int, optional): The number of greatest characters to return. Defaults to 76.
    Returns:
        list[str]: A sorted list of the top n greatest characters in the string based on their ASCII values.
    """

    # Create a dictionary to store the counts of each character
    char_counts = {}
    for char in s:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    # Sort the dictionary by value (frequency) and then by key (character)
    sorted_counts = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))

    # Return the top n greatest characters in the string based on their ASCII values
    return [char for char, count in sorted_counts[:n]]
