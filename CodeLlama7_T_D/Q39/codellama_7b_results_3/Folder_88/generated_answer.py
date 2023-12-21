
def return_n_greatest_chars(string, n=84):
    """
    Return the sorted list of exactly n characters of the given string that have the greatest ASCII values.
    Parameters:
        string (str): The input string.
        n (int, optional): The number of characters to return. Defaults to 84.
    Returns:
        List[str]: The sorted list of n characters with the greatest ASCII values.
    """

    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Sort the dictionary by value (frequency) in descending order
    sorted_dict = dict(sorted(char_freq.items(), key=lambda x: x[1], reverse=True))
    # Extract the top n characters with the greatest frequency and sort them in ascending order
    top_n_chars = list(sorted(list(sorted_dict.keys())[:n])))
    return top_n_chars
