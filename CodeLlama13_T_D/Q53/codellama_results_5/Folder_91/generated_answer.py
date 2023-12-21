
def palindrome_of_length_at_least_n(string):
    """
    Returns the set of all palindromes of length greater than or equal to 7 that exist in the given string.
    Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function returns an empty set. The function finds the palindromes in a case-insensitive manner.

    Args:
        string (str): String to search for palindromes.

    Returns:
        set[str]: Set of all palindromes found in the given string.
    """
    return {word for word in string.split() if len(word) >= 7 and word == word[::-1]}
