 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 4 in the given string
    for i in range(2, len(string) - 9 + 1):
        # Get the substring of length at least 4 starting from index i
        substr = string[i:i+4]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes found in the given string between indices 2 and 9 (inclusive)
    return palindromes
