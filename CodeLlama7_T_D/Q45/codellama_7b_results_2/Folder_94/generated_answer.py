
def palindromes_between_indices(string):
    # Define the range of indices to consider
    start_index = 3
    end_index = 4
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string within the specified range
    for i in range(start_index, end_index + 1):
        # Generate all possible palindromes of length at least 3 using the English letters in the given string that occur between index 3 to index 4, both inclusive
        for j in range(i - 2, i + 2):
            if (j >= start_index and j <= end_index) and (string[j] not in palindromes):
                # Form each palindrome in a case-insensitive manner
                palindrome = string[j].lower() + string[j - 1].lower() + string[j - 2].lower()
                if len(palindrome) >= 3:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of all palindromes of length at least 3 that can be created from the English letters of the given string within the specified range
    return palindromes
