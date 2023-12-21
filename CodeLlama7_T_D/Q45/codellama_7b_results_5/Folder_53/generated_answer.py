
def palindromes_between_indices(s):
    # Define the range of indices to consider
    start = 4
    end = 8
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the possible starting positions
    for i in range(start, end + 1):
        # Generate all possible palindromes of length at least 6
        for j in range(i, end + 1):
            # Check if the substring from index i to index j is a palindrome
            if s[i:j] == s[i:j][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(s[i:j])
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
