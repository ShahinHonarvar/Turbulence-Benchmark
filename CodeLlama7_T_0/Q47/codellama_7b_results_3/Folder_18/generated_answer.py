
def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(13, 67)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the range
    for length in lengths:
        # Get the substring starting from index 11 and ending at index 83 (inclusive)
        substring = string[11:84]
        # Find all palindromes of the current length in the substring
        palindromes_of_length = [word for word in substring.split() if len(word) == length and word.lower() == word[::-1].lower()]
        # Add the found palindromes to the set
        palindromes |= set(palindromes_of_length)
    return palindromes
