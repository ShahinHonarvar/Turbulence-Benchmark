
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length 7 or more in the given string
    for i in range(len(string) - 7 + 1):
        # Extract the current substring
        substr = string[i:i+7]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
