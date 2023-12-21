
def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible arrangement of the English letters in the given string that occur between index 3 to index 5, both inclusive
    for i in range(3, 6):
        # Iterate over each letter in the current position
        for j in input_string[i]:
            # Check if the current letter is a palindrome when reversed
            if j == j[::-1]:
                # Add the palindrome to the set
                palindromes.add(j)
    # Return the set of all palindromes of the length of at least 3 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 3 to index 5, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.
    return palindromes
