 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible combination of letters in the given string that occur between index 4 and index 9, both inclusive
    for i in range(4, 10):
        # Get the substring starting from index i to index i + 2 (since we want palindromes of length at least 3)
        substr = string[i:i+3]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
