
def return_nth_smallest_ascii(s):
    """
    Return the character with the 13th smallest ASCII value among those characters in the string that occur between indices 0 to 12, both inclusive.
    Args:
        s (string): The input string
    Returns:
        The character with the 13th smallest ASCII value
    """

    # Calculate the frequency of each ASCII value
    ascii_freq = {}
    for c in s:
        if c not in ascii_freq:
            ascii_freq[c] = 0
        ascii_freq[c] += 1
    # Sort the frequency dictionary by value
    sorted_freq = sorted(ascii_freq.items(), key=lambda x: x[1], reverse=True)
    # Get the character with the 13th smallest ASCII value
    char = sorted_freq[12][0]
    return char
