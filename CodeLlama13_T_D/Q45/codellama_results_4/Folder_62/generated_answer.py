
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each possible arrangement of English letters in the given string
    for i in range(len(string) - 8 + 1):
        # Extract a substring from index i to index i+8
        substr = string[i:i+9]

        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)

    # Return the set of all palindromes found
    return palindromes
