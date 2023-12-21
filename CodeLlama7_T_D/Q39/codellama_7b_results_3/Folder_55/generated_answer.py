
def return_n_greatest_chars(s: str, n: int) -> list[str]:
    """
    Return the sorted list of exactly n characters of the given string that have the greatest ASCII values.
    Args:
        s (str): The input string of distinct characters.
        n (int): The number of characters to return.
    Returns:
        list[str]: The sorted list of exactly n characters of the given string that have the greatest ASCII values.
    """

    # Create a dictionary to store the counts of each character in the input string
    char_counts = {}
    for char in s:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    # Sort the dictionary by value in descending order
    sorted_dict = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top n characters from the sorted dictionary
    return [char for char, count in sorted_dict[:n]]
