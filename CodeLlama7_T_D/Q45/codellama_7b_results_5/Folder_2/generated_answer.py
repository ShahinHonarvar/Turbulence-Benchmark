
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible starting index in the given string
    for i in range(len(string) - 5 + 1):
        # Extract a substring of length 6 from the given string, starting at the current index
        substr = string[i:i+6]
        # Check if the extracted substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
